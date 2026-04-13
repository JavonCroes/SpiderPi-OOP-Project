import cv2 as cv

from hardware.bus_servo import BusServo
from hardware.buzzer import Buzzer
from hardware.pwm_servo import PWMServo
from hardware.safety import SafetySystem
from vision.processor import FaceProcessor


def main():
    # HARDWARE TEST TOEGEVOEGD
    servo1 = BusServo(1)
    servo2 = PWMServo(2)
    buzzer = Buzzer()

    safety = SafetySystem([servo1, servo2], buzzer)

    servo1.move(90)
    servo2.set_angle(45)

    # temperatuur simulatie
    servo1.update_temperature(50)
    servo2.update_temperature(80)

    safety.check() 

    # Vision
    cap = cv.VideoCapture(0)
    
    tracker = FaceProcessor()

    print("AI Start! Druk op 'q' om te stoppen.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: 
            break

        frame, error_x = tracker.get_error(frame)

        if error_x != 0:
            print(f"Robot moet sturen: {error_x}")

        cv.imshow('SpiderPi Tracking', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
