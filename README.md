# GPIOLibrary

![pypi-badge](https://img.shields.io/pypi/v/robotframework-gpio)
![build-badge](https://api.travis-ci.com/ycbayrak/robotframework-gpio.svg)
![unstable](https://img.shields.io/static/v1?label=status&message=unstable&color=red)


Robot Framework Library for interfacing GPIO pins on executing robot files on Raspberry Pi's.

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


## Example

```robot
*** Settings ***

Documentation   Test LED is fully functional

Library                     Dialogs
Library                     GPIOLibrary

Suite Setup                 Begin GPIO Test

*** Variables ***

${LED_PIN}                  17

*** Test Cases ***

LED Should On
    Set Output Pin          ${LED_PIN}
    Set Pin High            ${LED_PIN}
    Execute Manual Step     "Is LED On?"

LED Should Off
    Set Output Pin          ${LED_PIN}
    Set Pin Low             ${LED_PIN}
    Execute Manual Step     "Is LED Off?"
    
 
*** Keywords ***

Begin GPIO Test
    Set Mode                BOARD
    Set Warnings Off
```

