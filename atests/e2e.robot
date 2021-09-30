*** Settings ***

Documentation   Test LED is fully functional

# Library                     Dialogs
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
    Set Output Pin          ${LED_PIN}
    Set Pin Low             ${LED_PIN}
    ${pin_status}=                  Get Pin Status      ${LED_PIN}
    Should Be Equal As Integers     ${pin_status}       1
 
*** Keywords ***

Begin GPIO Test
    Set Mode                BCM
    Set Warnings Off