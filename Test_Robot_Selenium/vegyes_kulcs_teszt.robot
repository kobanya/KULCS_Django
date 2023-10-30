*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:8000/
${BROWSER}    chrome
@{VALID_KEYS}    E07    E13
@{INVALID_KEYS}    1234    5678    91011    D27

*** Test Cases ***
Form Submission Test With Keys
    Open Browser    ${URL}    ${BROWSER}
    
    FOR    ${VALID_KEY}    IN    @{VALID_KEYS}
        Submit Form With Key    ${VALID_KEY}
        Verify Successful Submission    ${VALID_KEY}
    END

    FOR    ${INVALID_KEY}    IN    @{INVALID_KEYS}
        Submit Form With Key    ${INVALID_KEY}
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

Verify Successful Submission
    [Arguments]    ${KEY}
    Wait Until Page Contains Element    xpath=//table/tbody/tr[1]/td[contains(text(), 'Teszt Vezetéknév')]
    Wait Until Page Contains Element    xpath=//table/tbody/tr[1]/td[contains(text(), 'Teszt Keresztnév')]
    Wait Until Page Contains Element    xpath=//table/tbody/tr[1]/td[contains(text(), '${KEY}')]

Verify Error Message
    Wait Until Page Contains    A megadott kulcs nem érhető el!   timeout=10s
