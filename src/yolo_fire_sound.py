import cv2
import torch
import time
import threading
from playsound import playsound
import os

# Path to your YOLOv5 fire model (from this script's location)
MODEL_PATH = os.path.join(os.path.dirname(__file__),
                          r"..\yolov5-fire-detection\model\yolov5s_best.pt")

# Path to your alert sound file
ALERT_SOUND_PATH = os.path.join(os.path.dirname(__file__),
                                r"..\audio.wav")


is_playing_sound = False

def play_alert_sound():
    global _last_alert_time
    global is_playing_sound

    if is_playing_sound:
        return
    
    is_playing_sound = True

    def _play():
        global is_playing_sound
        try:
            playsound(ALERT_SOUND_PATH)
        except Exception as e:
            print(f"[WARN] couldn't play the sound: {e}")
        finally:
            is_playing_sound = False #we're done

    t = threading.Thread(target=_play, daemon=True) #call threading constructor to play
    t.start()

def main():
    model_path_abs = os.path.abspath(MODEL_PATH)
    sound_path_abs = os.path.abspath(ALERT_SOUND_PATH)

    print(f"Using model: {model_path_abs}")
    print(f"Using sound: {sound_path_abs}")

    if not os.path.exists(model_path_abs):
        print("[ERROR] YOLO model file not found!")
        return

    if not os.path.exists(sound_path_abs):
        print("[WARNING] Alert sound file not found, continuing without sound.")

    device = 'cuda' if torch.cuda.is_available() else 'cpu' #choosing device
    print(f"Loading model on device: {device}")

    #load model
    model = torch.hub.load(
        'ultralytics/yolov5',
        'custom',
        path=model_path_abs,
        source='github'
    ).to(device)

    model.conf = 0.25 #confidence threashold of model can be tweaked

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Could not open camera.")
        return

    print("[INFO] Press 'q' in the window to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] cannot read frames")
            break

        results = model(frame)

        detections = results.xyxy[0] # results.xyxy[0] is a tensor of detections: [x1, y1, x2, y2, conf, class]

        fire_detected = len(detections) > 0

        rendered_frame = results.render()[0].copy() #made change, openCV cannot use read only np array so used copy

        if fire_detected and os.path.exists(sound_path_abs):
            play_alert_sound()

        status_text = "FYNE SHIT" if fire_detected else "LOL"
        status_color = (0, 0, 255) if fire_detected else (0, 255, 0)

        cv2.putText(rendered_frame, status_text, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, status_color, 2, cv2.LINE_AA)
        
        cv2.imshow("YOLOv5 Fire Detector", rendered_frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()