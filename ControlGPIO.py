import RPi.GPIO as GPIO
import time


class ControlGPIO:
    def __init__(self, button_pin, is_input=True):
        GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme
        self.button_pin = button_pin
        if is_input:
            GPIO.setup(button_pin, GPIO.IN)
        else:
            GPIO.setup(button_pin, GPIO.OUT)

    def Interrupt(self, callback, bouncetime=100):
        GPIO.add_event_detect(
            self.button_pin,
            GPIO.FALLING,
            callback=callback,
            bouncetime=bouncetime,
        )

    def Set_Output(self, output):
        if output == 1:
            GPIO.output(self.button_pin, GPIO.HIGH)
        else:
            GPIO.output(self.button_pin, GPIO.LOW)

    def Check_Value(self, callback, check_value=0, bounce=100):
        value = GPIO.input(self.button_pin)
        if check_value == 0 and value == GPIO.LOW:
            callback()
            time.sleep(bounce / 1000)
        if check_value == 1 and value == GPIO.HIGH:
            callback()
            time.sleep(bounce / 1000)

    def Get_Value(self):
        value = GPIO.input(self.button_pin)
        return value

    def Cleanup(self):
        GPIO.cleanup()
