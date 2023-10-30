*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:8000/
${BROWSER}    chrome

*** Test Cases ***
Form Submission Test With Invalid Key
    Open Browser    ${URL}    ${BROWSER}
    Submit Form With Invalid Key
    Verify Error Message
    Close Browser

*** Keywords ***
Submit Form With Invalid Key
    Input Text    id=vezetek_nev    Teszt Vezetéknév
    Input Text    id=kereszt_nev    Teszt Keresztnév
    Input Text    id=kulcs_szam    1234
    Click Button    id=mentes

Verify Error Message
    Wait Until Page Contains    A megadott kulcs nem érhető el!   timeout=10s
