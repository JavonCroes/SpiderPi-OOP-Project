import cv2 as cv

from hardware.bus_servo import BusServo
from hardware.buzzer import Buzzer
from hardware.pwm_servo import PWMServo
from hardware.safety import SafetySystem
#from vision.processor import FaceProcessor
from vision.apriltag_processor import AprilTagProcessor
from utils.pid_controller import PID


def main():
    # HARDWARE TEST TOEGEVOEGD
    servo1 = BusServo(1)
    servo2 = PWMServo(2)
    buzzer = Buzzer()

    safety = SafetySystem([servo1, servo2], buzzer)

    servo1.move(90)
    servo2.set_angle(45)

    # temperatuur simulatie
    servo1.update_temperature(20)
    servo2.update_temperature(20)

    safety.check() 

    # Vision
    # cap = cv.VideoCapture(0)
    
    # tracker = FaceProcessor()

    # print("AI Start! Druk op 'q' om te stoppen.")

    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     if not ret: 
    #         break

    #     frame, error_x = tracker.get_error(frame)

    #     if error_x != 0:
    #         print(f"Robot moet sturen: {error_x}")

    #     cv.imshow('SpiderPi Tracking', frame)

    #     if cv.waitKey(1) & 0xFF == ord('q'):
    #         break

    # cap.release()
    # cv.destroyAllWindows()

    # 1. Hardware setup (Servo 1 = Pan, Servo 2 = Tilt)
    servo1 = BusServo(1)
    servo2 = PWMServo(2)
    # Startposities (Middenwaarde van de servo's)
    cur_p, cur_t = 500, 1500
    servo1.move(cur_p)
    servo2.set_angle(cur_t)
    # 2. Vision & PID setup
    cap = cv.VideoCapture(0)
    tracker = AprilTagProcessor()
    pid_x = PID(kp=0.08, ki=0.0, kd=0.01)
    pid_y = PID(kp=0.08, ki=0.0, kd=0.01)
    print("AprilTag Tracking Active... Press 'q' to stop.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: 
            break
        # 3. Detectie & Error berekening
        frame, ex, ey = tracker.get_error(frame)
        if ex != 0 or ey != 0:
            # 4. PID berekening en positie update
            cur_p -= pid_x.update(ex)
            cur_t += pid_y.update(ey)
            # Clamping (Voorkom dat de servo te ver draait)
            cur_p = max(0, min(1000, cur_p))
            cur_t = max(500, min(2500, cur_t))
            # 5. Hardware aansturen
            # In plaats van 500ms, gebruik 20ms of 0
            servo1.move(int(cur_p), 20)
            servo2.set_angle(int(cur_t))
        cv.imshow('SpiderPi Tracking', frame)
        if cv.waitKey(1) & 0xFF == ord('q'): 
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
