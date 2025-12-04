import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        frame = cv2.resize(frame, (640, 480))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # hsv has better color filtering

        #might need tweaking
        lower_fire = np.array([5, 120, 120])   # H, S, V
        upper_fire = np.array([35, 255, 255])  # about orange/yellow range

        mask = cv2.inRange(hsv, lower_fire, upper_fire) #create mask in range

        #clean a bit of noise
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        fire_detected = False

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 800:   #ignore small stuff; tweak this number
                fire_detected = True
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, "Fire?", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        #Put overall status text
        if fire_detected:
            text = "FLAME DETECTED"
            color = (0, 0, 255)
        else:
            text = "No flame"
            color = (0, 255, 0)

        cv2.putText(frame, text, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 2, cv2.LINE_AA)

        #Show windows
        cv2.imshow("Fire Detector", frame)
        cv2.imshow("Fire Mask", mask)

        #quit on q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()