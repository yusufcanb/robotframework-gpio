import RPi.GPIO as GPIO

from robot.api.deco import keyword


class GPIOKeywords(object):
    @keyword("Set Input Pin")
    def set_input_pin(self, channel):
        """
        Setup GPIO channel or list of channels as input.
        """
        GPIO.setup(channel, GPIO.IN)

    @keyword("Set Output Pin")
    def set_output_pin(self, channel):
        """
        Setup GPIO channel or list of channels as output.
        """
        GPIO.setup(channel, GPIO.OUT)
