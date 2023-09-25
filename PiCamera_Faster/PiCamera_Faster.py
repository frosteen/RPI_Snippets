from imutils.video.pivideostream import PiVideoStream
import cv2

cap = PiVideoStream(resolution=(1280, 720), framerate=60).start()

while True:
    frame = cap.read()

    if frame is None:
        continue

    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Frame", int(1280 * 0.5), int(720 * 0.5))
    cv2.imshow("Frame", frame)

    # ESC to quit
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        break

# do a bit of cleanup
cap.stop()
cv2.destroyAllWindows()
