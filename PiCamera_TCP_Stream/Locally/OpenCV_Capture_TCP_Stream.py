import cv2

# Run the following below on RPI then connect by running this python code
# sh Raspistill_TCP_Stream.sh
# or
# sh libcamera-vid_TCP_Stream.sh

cap = cv2.VideoCapture("tcp://raspberrypitraffic.local:5000")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame5
    cv2.imshow("frame", frame)

    # ESC to quit
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
