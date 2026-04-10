import time

from gpiozero import Buzzer as GZ_Buzzer


class Buzzer:
    def __init__(self, gpio_pin=None):
        self.gpio_pin = gpio_pin
        self.device = None

        if self.gpio_pin is not None:
            try:
                self.device = GZ_Buzzer(self.gpio_pin)
            except Exception as e:
                print(f"Buzzer hardware niet gevonden: {e}")

    def beep(self, duration=0.2):
        if self.device:
            self.device.on()
            time.sleep(duration)
            self.device.off()
        else:
            # Valt terug op simulatie als er geen pin of hardware is
            print("🔔 simulatie beep (geen hardware gevonden)")
