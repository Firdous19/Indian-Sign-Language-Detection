import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import torch
from model import SpatialISLTransformer

HAND_CONNECTIONS =[(0,1), (1,2), (2,3), (3,4), (0,5), (5,6), (6,7), (7,8), 
                    (5,9), (9,10), (10,11), (11,12), (9,13), (13,14), (14,15), 
                    (15,16), (13,17), (17,18), (18,19), (19,20), (0,17)]

class StaticISLDetector:
    def __init__(self, model_path="isl_model.pth", classes_path="classes.npy", task_path="hand_landmarker.task"):
        self.labels = np.load(classes_path, allow_pickle=True)
        self.num_classes = len(self.labels)
        
        base_options = python.BaseOptions(model_asset_path=task_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=2,
            min_hand_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.hand_detector = vision.HandLandmarker.create_from_options(options)
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = SpatialISLTransformer(num_classes=self.num_classes).to(self.device)
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.eval()

    def draw_custom_landmarks(self, frame, hand_landmarks):
        h, w, _ = frame.shape
        points =[]
        for lm in hand_landmarks:
            px, py = int(lm.x * w), int(lm.y * h)
            points.append((px, py))
            
        for p1, p2 in HAND_CONNECTIONS:
            cv2.line(frame, points[p1], points[p2], (0, 255, 0), 2)
            
        for p in points:
            cv2.circle(frame, p, 4, (0, 0, 255), -1)

    def predict_frame(self, frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
        
        results = self.hand_detector.detect(mp_image)
        
        features = np.zeros((42, 3), dtype=np.float32)
        hand_detected = False
        
        if results.hand_landmarks:
            hand_detected = True
            for idx in range(len(results.hand_landmarks)):
                hand_landmarks = results.hand_landmarks[idx]
                handedness = results.handedness[idx][0].category_name
                
                offset = 0 if handedness == 'Left' else 21
                
                # EXACT SAME NORMALIZATION AS TRAINING
                hand_coords = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks])
                wrist_coord = hand_coords[0]
                hand_coords = hand_coords - wrist_coord
                max_val = np.max(np.abs(hand_coords))
                if max_val > 0:
                    hand_coords = hand_coords / max_val
                    
                features[offset : offset + 21] = hand_coords
                self.draw_custom_landmarks(frame, hand_landmarks)
                
        if not hand_detected:
            return "No Hand Detected", 0.0, frame

        input_tensor = torch.tensor(features).unsqueeze(0).to(self.device)
        with torch.no_grad():
            outputs = self.model(input_tensor)
            probabilities = torch.softmax(outputs, dim=1)
            max_prob, predicted_idx = torch.max(probabilities, dim=1)
            
            confidence = max_prob.item()
            prediction = self.labels[predicted_idx.item()]
            
            # Increased threshold since normalized data is much more accurate
            if confidence < 0.60:
                prediction = "Unknown Sign"
                
        return prediction, confidence, frame