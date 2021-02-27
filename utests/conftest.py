import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(os.path.join(dir_path, os.pardir))

sys.path.insert(0, os.path.join(dir_path, os.pardir, "src"))

import pytest
