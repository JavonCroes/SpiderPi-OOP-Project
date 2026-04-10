from hardware.actuator import Actuator

class PWMServo(Actuator):

    def set_angle(self, angle):
        print(f"PWMServo {self.id} -> {angle}")