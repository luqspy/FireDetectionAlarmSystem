# Fire Detection Alarm System

**Real-time flame detection using YOLOv5 + Python + OpenCV + Audio Alerts**

This project detects fire using a webcam and triggers an audio alarm whenever fire is detected. It is built using **YOLOv5**, **OpenCV**, and **PyTorch**, with a smooth non-overlapping sound system that only plays the alert once per detection cycle.

---



## Features

* **Real-time** fire detection using YOLOv5.
* **Audio alarm system** that does not overlap.
* **Sound repeats** only when the previous sound is fully finished.
* **Custom logic** to prevent spam or rapid triggering.
* **Lightweight**, minimal project structure.
* **Non-blocking** threaded audio playback.
* **Built-in camera** test script.
* **Clean**, beginner-friendly folder structure.

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

```
FireDetectionAlarmSystem/
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
└── README.md
```

## Clone this repo


```
git clone https://github.com/luqspy/FireDetectionAlarmSystem

cd FireDetectionAlarmSystem

```
## Install Dependencies

```
pip install -r Requirements/requirements.txt
```
## Running the Fire Detector
From the root folder:
```
cd src

python yolo_fire_sound.py
```
**This will:**
  
  1. Open your webcam
  
  2. Run YOLOv5 fire detection
  
  3. Draw bounding boxes
  
  4. Play your alert sound whenever fire is detected
  
  5. Press Q to quit.

## Audio Alarm Behavior

**The alarm system is designed to be smooth and non-spammy:**

  1. When fire is detected → play one full sound
  
  2. While sound is playing → no new sounds play
  
  3. When sound finishes:
  
      a. If fire is still visible → play again
  
      b. If fire is gone → stay silent

This gives a natural “fire alarm loop” without glitching or overlap.

##Camera Test
```
python test_camera.py
```
##How it Works

**YOLOv5 Model**
The project loads YOLOv5 from Torch Hub:
```
torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

```
**Fire Detection**

The model outputs bounding boxes whenever it sees fire-like objects.

**Audio Logic**

A small state machine ensures:

  1. No overlapping sounds
  
  2. Full playback
  
  3. Re-trigger only after playback ends
  
  4. Optional cooldown (not needed but easy to add)

##Credits

**YOLOv5**

Ultralytics YOLOv5 (Apache License 2.0)
https://github.com/ultralytics/yolov5

**Fire Model**

Fire YOLOv5 weights sourced from:
https://github.com/spacewalk01/yolov5-fire-detection
(Or your trained variant)

If you use their weights, keep their **LICENSE** in your repo.

