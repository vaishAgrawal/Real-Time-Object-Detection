🎯 Real-Time Object Detection with YOLO 🚀

Welcome to my Real-Time Object Detection project! 👋
This application uses YOLO (You Only Look Once), 
a state-of-the-art object detection model, 
to detect objects in real-time from your webcam feed.

It’s designed to showcase my skills in Artificial Intelligence, Python, and Computer Vision, while providing a clean and interactive user experience.


📜 About This Project
This project demonstrates my ability to build AI-powered real-time applications using deep learning models.


🧠 Artificial Intelligence (AI)

📸 Computer Vision (CV)

💻 Python Development

🌟 What this app does:
✅ Detects multiple objects in real-time from your webcam
✅ Draws bounding boxes and labels with confidence scores
✅ Provides a simple and clean UI for interaction

🚀 Technologies Used
Technology	Purpose
Python 3.x	Backend logic and machine learning
YOLOv8	Object detection model (Ultralytics)
PyTorch	Deep Learning Framework
OpenCV	Webcam integration & image processing
Streamlit For web-based UI

✨ Features
💡 Real-Time Object Detection – Uses webcam feed for live object recognition

📦 Portable – Works on any machine with minimal setup

🖥️ Clean UI – Beginner-friendly and visually appealing

🔗 Open Source – Ready for contributions and upgrades

📁 Folder Structure

real-time-object-detection/
│
├── yolov8n.pt           
├── yolo_webcam.py        
├── requirements.txt      
├── README.md             
└── assets/               

🛠️ Installation & Setup
1️⃣ Clone the repository

git clone https://github.com/vaishAgrawal/Real-Time-Object-Detection.git
cd Real-Time-Object-Detection

2️⃣ Create a virtual environment

python -m venv venv
venv\Scripts\activate     

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Download YOLOv8 weights

Get the YOLOv8 pretrained weights (yolov8n.pt) from Ultralytics
and place it in the project directory.

🚦 Usage
▶️ Run the application

python yolo_webcam.py
📌 The webcam will open and start detecting objects in real-time.
🔴 Press Q to quit the webcam window.
