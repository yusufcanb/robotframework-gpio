# GPIOLibrary

![pypi-badge](https://img.shields.io/pypi/v/robotframework-gpio)
[![build](https://github.com/yusufcanb/robotframework-gpio/actions/workflows/python-build.yml/badge.svg?branch=master)](https://github.com/yusufcanb/robotframework-gpio/actions/workflows/python-build.yml)
![stable](https://img.shields.io/static/v1?label=status&message=stable&color=green)


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

