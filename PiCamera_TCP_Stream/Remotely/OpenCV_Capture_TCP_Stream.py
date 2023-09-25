import cv2

# Run the following below on RPI then connect by running this python code
# sh Raspistill_TCP_Stream.sh
# or
# sh libcamera-vid_TCP_Stream.sh
# python3 Ngrok_Notify.py

cap = cv2.VideoCapture(
    "tcp://6.tcp.ngrok.io:15008"
)  # get link from email sent by Ngrok_Notify.py

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        continue

    # Display the resulting frame5
    cv2.imshow("frame", frame)

    # ESC to quit
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
