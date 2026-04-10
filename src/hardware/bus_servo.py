from hardware.actuator import Actuator

class BusServo(Actuator):

    def move(self, position, time=500):
        print(f"BusServo {self.id} -> {position} in {time}ms")

    def read_position(self):
        return 500  # placeholder