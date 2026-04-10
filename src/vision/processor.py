import cv2 as cv


class VisionProcessor:
    def __init__(self):
        self.cap = cv.VideoCapture(0)

        self.face_cascade = cv.CascadeClassifier("vision/haar_face.xml")

        self.error_x = 0

    @property
    def target_x(self):
        return self.error_x

    def find_face(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.05, 6, minSize=(30, 30))

        # Midden van het scherm
        scherm_midden = frame.shape[1] // 2

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            gezicht_midden = x + (w // 2)

            # De math
            self.error_x = gezicht_midden - scherm_midden

            # draw groene box
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            self.error_x = 0

        return frame

    def stop(self):
        self.cap.release()
