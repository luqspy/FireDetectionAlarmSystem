import cv2

def main():
    cap = cv2.VideoCapture(0) # default camera

    if not cap.isOpened():
        print("Can't open camera")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't read frames")
            break

        
        cv2.imshow("Camera Test - Press q to quit", frame)

        # wait 1 ms, quit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()