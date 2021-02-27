*** Settings ***

Documentation   Test for GPIO Interface
Library  GPIOLibrary
Library  BuiltIn

*** Test Cases ***

Board Keywords Should Be Exists
    Keyword Should Exist    Set Mode
    Keyword Should Exist    Get Mode
    Keyword Should Exist    Clean Up Board
    Keyword Should Exist    Set Warnings On
    Keyword Should Exist    Set Warnings Off