# 🤟 Gestura: Indian Sign Language (ISL) Translation System

Gestura is a real-time computer vision application designed to bridge the communication gap between the hearing-impaired community and the general public. By leveraging Deep Learning and MediaPipe, the system translates Indian Sign Language (ISL) static gestures into text and audible speech.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=Streamlit\&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge\&logo=PyTorch\&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge\&logo=OpenCV\&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-00C7B7?style=for-the-badge\&logo=google\&logoColor=white)

---

## 🚀 Key Features

* **Real-time Gesture Recognition:** High-speed translation using a local webcam feed.
* **MediaPipe Integration:** Precise 21-point hand landmark detection for robust tracking.
* **Sentence Builder:** Intelligent logic to concatenate individual signs into full words and sentences.
* **Text-to-Speech (TTS):** Integrated audio feedback to "speak" the translated signs.
* **Dynamic UI:** A modern, responsive dashboard built with Streamlit.
* **Interactive Controls:** In-app buttons for Space, Delete, Clear, and Speak to manage constructed text.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Computer Vision:** [OpenCV](https://opencv.org/) & [MediaPipe](https://google.github.io/mediapipe/)
* **Deep Learning Framework:** [PyTorch](https://pytorch.org/)
* **Data Processing:** [NumPy](https://numpy.org/)
* **Audio:** [PyTTSx3](https://pyttsx3.readthedocs.io/)

---

## 📂 Project Structure

```text
ISL_TRASN/
├── dataset/                # Raw image data for training
├── pages/
│   └── Translate.py        # Main Translation Application page
|   └── About.py
|   └── Home.py
├── venv/                   # Python Virtual Environment
├── app.py                  # Landing page/Entry point
├── detector.py             # Logic for Hand Detection & Prediction
├── model.py                # Neural Network Architecture (PyTorch)
├── prepare_data.py         # Script to process images into NumPy arrays
├── train.py                # Script to train the ISL model
├── utils.py                # UI components and helper functions
├── isl_model.pth           # Trained PyTorch Model weights
├── hand_landmarker.task    # MediaPipe Hand Landmarker model
├── classes.npy             # Label names (A, B, C, etc.)
├── requirements.txt        # Project dependencies
└── .gitignore              # Files to be ignored by Git
```

---

## ⚙️ Installation & Setup

### Clone the repository:

```bash
git clone https://github.com/Firdous19/Indian-Sign-Language-Detection.git
cd Indian-Sign-Language-Detection
```

### Create and Activate Virtual Environment:

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Run the Application:

```bash
streamlit run app.py
```

---

## 📸 Usage Guide

* **Launch the App:** Once the server starts, navigate to the Translate page in the sidebar.
* **Activate Camera:** Toggle the "Active" switch in the Video Input section.
* **Perform Signs:** Place your hand in the frame. The system will detect landmarks and show the predicted label.

### Build Sentences:

* Hold a sign for 10 frames to "commit" the character.
* Use the Space button to separate words.
* Use the Speak button to hear the final sentence.

---

## 🧠 Model Information

* The system uses a custom-trained Neural Network built with PyTorch.
* **Input:** 21 hand landmarks (x, y, z coordinates) extracted via MediaPipe.
* **Output:** Classification into specific ISL alphabets/words defined in `classes.npy`.

### Training:

To retrain the model:

```bash
python train.py
```

(Ensure images are placed inside the `dataset/` folder)

---

## 🚧 Future Scope

* Support for dynamic/motion-based signs (moving hands).
* Integration of a Transformer-based Language Model for better grammar correction.
* Mobile application deployment using Flutter or React Native.
* Multi-hand support for complex signs.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please open an issue or submit a pull request.

---

Developed with ❤️ by team.
