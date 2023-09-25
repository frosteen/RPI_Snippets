import io

import cv2
import numpy as np
from picamera import PiCamera

with PiCamera() as camera:
    camera.resolution = (3280, 2464)
    # camera.resolution = camera.MAX_IMAGE_RESOLUTION  # The following is equivalent
    stream = io.BytesIO()  # stream via buffer to mitigate rpi memory issue
    for _ in camera.capture_continuous(stream, format="png"):
        data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
        frame = cv2.imdecode(data, 1)
        stream.seek(0)
        stream.truncate()

        cv2.imshow("frame", frame)

        # ESC to quit
        key = cv2.waitKey(1)
        if key & 0xFF == 27:
            break

    # When everything done, release the capture
    cv2.destroyAllWindows()
