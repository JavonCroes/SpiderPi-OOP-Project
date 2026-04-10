import cv2 as cv
from hardware.bus_servo import BusServo
from hardware.buzzer import Buzzer
from hardware.pwm_servo import PWMServo
from hardware.safety import SafetySystem
from vision.processor import VisionProcessor


def main():
    #HARDWARE TEST TOEGEVOEGD
    servo1 = BusServo(1)
    servo2 = PWMServo(2)
    buzzer = Buzzer(gpio_pin=16)

    safety = SafetySystem([servo1, servo2], buzzer)

    servo1.move(90)
    servo2.set_angle(45)

    #temperatuur simulatie 
    servo1.update_temperature(50)
    servo2.update_temperature(80)

    safety.check()  # 🔥 moet warning geven

    robot_oog = VisionProcessor()

    print("Robot kijkt nu... Druk op 'q' om te stoppen.")

    while True:
        beeld = robot_oog.find_face()

        if beeld is not None:
            afwijking = robot_oog.target_x

            if afwijking != 0:
                print(f"Gezicht gevonden! Afwijking: {afwijking} pixels")

            cv.imshow("SpiderPi", beeld)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    robot_oog.stop()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
