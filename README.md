# GPIOLibrary

![pypi-badge](https://img.shields.io/pypi/v/robotframework-gpio)
[![build](https://github.com/yusufcanb/robotframework-gpio/actions/workflows/python-build.yml/badge.svg?branch=master)](https://github.com/yusufcanb/robotframework-gpio/actions/workflows/python-build.yml)
![stable](https://img.shields.io/static/v1?label=status&message=stable&color=green)


Robot Framework Library for interfacing GPIO pins on executing robot files on Raspberry Pi's.

For Library documentation you can visit; [https://yusufcanb.github.io/robotframework-gpio/](https://yusufcanb.github.io/robotframework-gpio/)

## Requirements

- [Robot Framework (^3.2.2) ](https://pypi.org/project/robotframework/)
- [RPi.GPIO (^0.7.0)](https://pypi.org/project/RPi.GPIO/)

## Installation

Install [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) with command below;

```
pip install RPi.GPIO
```

Then install GPIOLibrary with;

```shell
pip install robotframework-gpio
```


## Examples

You can find example robot files in the `/examples` directory.

### Basic Usage

```robot
*** Settings ***

Documentation   Test LED is fully functional
Library                     GPIOLibrary
Suite Setup                 Begin GPIO Test

*** Variables ***

${LED_PIN}                  17

*** Test Cases ***

LED Should On
    Set Output Pin                  ${LED_PIN}
    Set Pin High                    ${LED_PIN}
    ${pin_status}=                  Get Pin Status      ${LED_PIN}
    Should Be Equal As Integers     ${pin_status}       1

LED Should Off
    Set Output Pin                  ${LED_PIN}
    Set Pin Low                     ${LED_PIN}
    ${pin_status}=                  Get Pin Status      ${LED_PIN}
    Should Be Equal As Integers     ${pin_status}       1
 
*** Keywords ***

Begin GPIO Test
    Set Mode                        BCM
    Set Warnings Off
```


### Remote Library Usage

First install robotframework/PythonRemoteServer to Raspberry Pi;

```
pip install robotremoteserver
```


Then, start remote library server with following commands;

```python
from robotremoteserver import RobotRemoteServer
from GPIOLibrary import GPIOLibrary

RobotRemoteServer(GPIOLibrary(), host='0.0.0.0')
```

Finally, you can execute the robot file below from any machine within the same network of Raspberry Pi.


``` robot
*** Settings ***

Documentation                       Example robot file for using GPIOLibrary on a remote Raspberry Pi device

Library                             Remote      http://${ADDRESS}:${PORT}
Library                             Dialogs
Suite Setup                         Begin GPIO Test

*** Variables ***

${ADDRESS}    raspberrypi.local
${PORT}       8270

${LED_PIN}                          17

*** Test Cases ***

LED Should On
    Set Output Pin                  ${LED_PIN}
    Set Pin High                    ${LED_PIN}
    Execute Manual Step             LED is on?
    

LED Should Off
    Set Output Pin                  ${LED_PIN}
    Set Pin Low                     ${LED_PIN}
    Execute Manual Step             LED is off?
 
*** Keywords ***

Begin GPIO Test
    Set Mode                        BCM
    Set Warnings Off

```
