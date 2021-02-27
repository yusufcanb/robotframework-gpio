import RPi.GPIO as GPIO

from robot.api.deco import keyword


class BoardKeywords(object):
    @keyword("Get Mode")
    def get_mode(self, mode):
        """
        Gets board numbering mode. Either BCM or BOARD
        """
        return GPIO.getmode()

    @keyword("Set Mode")
    def set_mode(self, mode):
        """
        Sets board numbering mode. Either BCM or BOARD
        """
        if not mode in ["BCM", "BOARD"]:
            raise Exception("Mode is not present. Valid choices are: [BCM, BOARD]")
        GPIO.setmode(mode)

    @keyword("Set Warnings On")
    def set_warnings_on(self):
        """
        Enable GPIO usage warnings.
        """
        GPIO.setwarnings(True)

    @keyword("Set Warnings Off")
    def set_warnings_off(self):
        """
        Disable GPIO usage warnings.
        """
        GPIO.setwarnings(False)

    @keyword("Clean Up Board")
    def clean_up_board(self):
        """
        Resets board to initial state.
        """
        GPIO.cleanup()
