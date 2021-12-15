*** Settings ***

Documentation   Test for GPIO Interface
Library         GPIOLibrary

*** Test Cases ***

GPIO Keywords Should Be Exists
    Keyword Should Exist    Set Input Pin
    Keyword Should Exist    Set Output Pin

    Keyword Should Exist    Set Pin High
    Keyword Should Exist    Is Pin High

    Keyword Should Exist    Set Pin Low
    Keyword Should Exist    Is Pin Low

    Keyword Should Exist    Get Pin Status
