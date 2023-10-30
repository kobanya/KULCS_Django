*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:8000/
${BROWSER}    chrome
@{KEYS}    1234    5678    91011    1213 D12  Z35 K49 U17 D89 K38 Z17

*** Test Cases ***
Form Submission Test With Invalid Keys
    Open Browser    ${URL}    ${BROWSER}
    FOR    ${KEY}    IN    @{KEYS}
        Submit Form With Key    ${KEY}
        Verify Error Message
    END
    Close Browser

*** Keywords ***
Submit Form With Key
    [Arguments]    ${KEY}
    Input Text    id=vezetek_nev    Teszt Vezetéknév
    Input Text    id=kereszt_nev    Teszt Keresztnév
    Input Text    id=kulcs_szam    ${KEY}
    Click Button    id=mentes

Verify Error Message
    Wait Until Page Contains    A megadott kulcs nem érhető el!   timeout=10s
