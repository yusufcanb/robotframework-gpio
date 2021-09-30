import RPi.GPIO as GPIO

from robot.api.deco import keyword


class GPIOKeywords(object):
    @keyword("Set Input Pin")
    def set_input_pin(self, channel: str):
        """
        Setup GPIO channel or list of channels as input.
        """
        GPIO.setup(int(channel), GPIO.IN)

    @keyword("Set Output Pin")
    def set_output_pin(self, channel: str):
        """
        Setup GPIO channel or list of channels as output.
        """
        GPIO.setup(int(channel), GPIO.OUT)

    @keyword("Set Pin High")
    def set_pin_high(self, channel: str):
        """
        """
        GPIO.output(int(channel), GPIO.HIGH)

    @keyword("Set Pin Low")
    def set_pin_low(self, channel: str):
        """
        """
        GPIO.output(int(channel), GPIO.LOW)

    @keyword("Get Pin Status")
    def get_pin_status(self, channel: str):
        """
        """
        return GPIO.input(int(channel))