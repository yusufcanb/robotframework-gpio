*** Settings ***

Documentation   Test for GPIO Interface
Library  GPIOLibrary

*** Test Cases ***

GPIO Keywords Should Be Exists
    Keyword Should Exist    Set Input Pin
    Keyword Should Exist    Set Output Pin
