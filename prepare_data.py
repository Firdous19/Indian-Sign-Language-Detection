import os
import urllib.request
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tqdm import tqdm

def download_model():
    model_path = 'hand_landmarker.task'
    if not os.path.exists(model_path):
        print("Downloading MediaPipe Hand Landmarker model...")
        url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task"
        urllib.request.urlretrieve(url, model_path)
    return model_path

def extract_landmarks_from_dataset(dataset_path="dataset"):
    model_path = download_model()
    
    base_options = python.BaseOptions(model_asset_path=model_path)
    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        num_hands=2,
        min_hand_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    detector = vision.HandLandmarker.create_from_options(options)
    
    X = []
    y =[]
    
    classes = sorted(os.listdir(dataset_path))
    print(f"Found classes: {classes}")
    
    for label in classes:
        class_dir = os.path.join(dataset_path, label)
        if not os.path.isdir(class_dir):
            continue
            
        for img_name in tqdm(os.listdir(class_dir), desc=f"Processing {label}"):
            img_path = os.path.join(class_dir, img_name)
            image = cv2.imread(img_path)
            if image is None:
                continue
                
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
            detection_result = detector.detect(mp_image)
            
            features = np.zeros((42, 3), dtype=np.float32)
            
            if detection_result.hand_landmarks:
                for idx in range(len(detection_result.hand_landmarks)):
                    hand_landmarks = detection_result.hand_landmarks[idx]
                    handedness = detection_result.handedness[idx][0].category_name
                    
                    offset = 0 if handedness == 'Left' else 21
                    
                    # 1. Extract raw coordinates
                    hand_coords = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks])
                    
                    # 2. Normalize (Subtract wrist coordinate to make it location invariant)
                    wrist_coord = hand_coords[0]
                    hand_coords = hand_coords - wrist_coord
                    
                    # 3. Scale (Divide by max absolute value to make it size invariant)
                    max_val = np.max(np.abs(hand_coords))
                    if max_val > 0:
                        hand_coords = hand_coords / max_val
                        
                    features[offset : offset + 21] = hand_coords
                
                X.append(features)
                y.append(label)

    X = np.array(X)
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    np.save("X.npy", X)
    np.save("y.npy", y_encoded)
    np.save("classes.npy", le.classes_)
    
    print(f"\nExtracted {len(X)} samples successfully! (NORMALIZED DATA)")

if __name__ == "__main__":
    extract_landmarks_from_dataset()