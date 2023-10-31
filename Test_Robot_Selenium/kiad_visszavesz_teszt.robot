*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:8000/
${BROWSER}    chrome

*** Test Cases ***
Form Submission Test
    Open Browser    ${URL}    ${BROWSER}
    Submit Form
    Return Key
    Close Browser

*** Keywords ***
Submit Form
    Input Text    id=vezetek_nev    Teszt Vezetéknév
    Input Text    id=kereszt_nev    Teszt Keresztnév
    Input Text    id=kulcs_szam     E07
    Click Button    id=mentes



Return Key
    # Várakozás a "Teszt Vezetéknév" szöveg megjelenésére
    Wait Until Page Contains    Teszt Vezetéknév    timeout=10s
    Wait Until Element Is Enabled    xpath=//input[@value='Visszaadva']    timeout=10s
    Click Element    xpath=//input[@value='Visszaadva']
