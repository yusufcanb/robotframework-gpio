*** Settings ***

Documentation                       Example robot file for using GPIOLibrary on a remote Raspberry Pi device

Library                             Remote      http://${ADDRESS}:${PORT}
Library                             Dialogs
Suite Setup                         Begin GPIO Test

*** Variables ***

${ADDRESS}                          raspberrypi.local
${PORT}                             8270

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
