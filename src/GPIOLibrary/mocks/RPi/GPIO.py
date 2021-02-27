"""
Mock module for RPi.GPIO
Makes it easy to development on non ARM architectures.
"""

import time
import logging

from ..RPi import (
    BCM,
    BOARD,
    BOTH,
    PUD_OFF,
    PUD_UP,
    PUD_DOWN,
    OUT,
    IN,
    I2C,
    LOW,
    SPI,
    HIGH,
    SERIAL,
    RISING,
    HARD_PWM,
    FALLING,
    UNKNOWN,
    VERSION,
    RPI_INFO,
    RPI_REVISION,
)

logger = logging.getLogger(__name__)

_mode = 0

channel_config = {}
setModeDone = False


class Channel:
    def __init__(self, channel, direction, initial=0, pull_up_down=PUD_OFF):
        self.channel = channel
        self.direction = direction
        self.initial = initial
        self.pull_up_down = pull_up_down


def setmode(mode):
    time.sleep(0.5)
    if mode == BCM:
        setModeDone = True
        _mode = mode

    elif mode == BOARD:
        setModeDone = True
    else:
        setModeDone = False


def getmode():
    return _mode


def setwarnings(flag):
    logger.info("setwarnings::{}".format(flag))


def setup(channel, direction, initial=0, pull_up_down=PUD_OFF):
    logger.info(
        "setup::{}, {}, initial={}, pull_up_down={}".format(
            channel, direction, initial, pull_up_down
        )
    )
    global channel_config
    channel_config[channel] = Channel(channel, direction, initial, pull_up_down)


def output(channel, value):
    logger.info("output::{}, {}".format(channel, value))


def input(channel):
    logger.info("input::{}".format(channel))


def wait_for_edge(channel, edge, bouncetime, timeout):
    logger.info(
        "wait_for_edge::{}, {}, {}, {}".format(edge, channel, bouncetime, timeout)
    )


def add_event_detect(channel, edge, callback, bouncetime):
    logger.info(
        "add_event_detect::{}, {}, {}, {}".format(edge, channel, bouncetime, callback)
    )


def event_detected(channel):
    logger.info("event_detected::{}".format(channel))


def add_event_callback(channel, callback):
    logger.info("add_event_callback::{}, {}".format(callback, channel))


def remove_event_detect(channel):
    logger.info("remove_event_detect::{}".format(channel))


def gpio_function(channel):
    logger.info(
        "gpio_function::{}, {}".format(channel, channel_config[channel].direction)
    )


class PWM:
    def __init__(self, channel, frequency):
        self.channel = channel
        self.frequency = frequency
        self.duty_cycle = 0
        global channel_config
        channel_config[channel] = Channel(
            channel,
            PWM,
        )

    def start(self, duty_cycle):
        self.duty_cycle = duty_cycle
        logger.info(
            "PWM::start::{} with Duty cycle : {}".format(self.channel, duty_cycle)
        )

    def ChangeFrequency(self, frequency):
        logger.info("PWM::ChangeFrequency::{}, {}".format(self.channel, frequency))
        self.frequency = frequency

    def ChangeDutyCycle(self, duty_cycle):
        self.duty_cycle = duty_cycle
        logger.info("PWM::ChangeFrequency::{}, {}".format(self.channel, duty_cycle))

    def stop(self):
        logger.info("PWM::stop::{}, {}".format(self.channel, self.duty_cycle))


def cleanup(channel=None):
    logger.info("GPIO::cleanup::{}".format(channel))
