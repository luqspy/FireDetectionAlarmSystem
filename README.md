# Fire Detection Alarm System

**Real-time flame detection using YOLOv5 + Python + OpenCV + Audio Alerts**

This project detects fire using a webcam and triggers an audio alarm whenever fire is detected. It is built using **YOLOv5**, **OpenCV**, and **PyTorch**, with a smooth non-overlapping sound system that only plays the alert once per detection cycle.

---



## Features

* **🎥 Real-time** fire detection using YOLOv5.
* **🔊 Audio alarm system** that does not overlap.
* **🔁 Sound repeats** only when the previous sound is fully finished.
* **🧠 Custom logic** to prevent spam or rapid triggering.
* **📦 Lightweight**, minimal project structure.
* **⚙️ Non-blocking** threaded audio playback.
* **🔍 Built-in camera** test script.
* **📁 Clean**, beginner-friendly folder structure.

---

## Tech Stack

| Component | Purpose |
| :--- | :--- |
| **Python** 3.10+ | Core programming language. |
| **PyTorch** | Deep learning framework. |
| **YOLOv5** (via Torch Hub) | State-of-the-art object detection model. |
| **OpenCV** | Reading video streams and drawing bounding boxes. |
| **NumPy** | Numerical operations. |
| **playsound** | Handling audio playback. |

---

## Folder Structure

'''FireDetectionAlarmSystem/
│
├── src/
│   ├── yolo_fire_sound.py          # Main detector + alarm logic
│   ├── test_camera.py              # Test webcam
│   └── fire_detection.py           # Optional extra scripts
│
├── model/
│   └── yolov5s_best.pt             # Fire-detection YOLO model weights
│
├── Requirements/
│   └── requirements.txt
│
├── assets/
│   └── alert.wav                   # Alarm sound file (you provide)
│
└── README.md'''
