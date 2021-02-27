import os
import sys

try:
    import RPi.GPIO

except ImportError:
    if os.uname()[4][:3] == "arm":
        raise ImportError("No module named RPi.GPIO")

    from .mocks import RPi
    from .mocks.RPi import GPIO

    sys.modules["RPi"] = RPi
    sys.modules["RPi.GPIO"] = GPIO

from GPIOLibrary.keywords import BoardKeywords, GPIOKeywords

__version___ = "0.1.0-beta1"


class GPIOLibrary(BoardKeywords, GPIOKeywords):
    __version__ = __version___

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
