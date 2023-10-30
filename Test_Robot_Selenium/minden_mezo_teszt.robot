*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:8000/
${BROWSER}    chrome

*** Test Cases ***
Verify Required Fields
    Open Browser    ${URL}    ${BROWSER}
    ${vezetek_required}=    Get Element Attribute    id=vezetek_nev    required
    ${kereszt_required}=    Get Element Attribute    id=kereszt_nev    required
    ${kulcs_required}=    Get Element Attribute    id=kulcs_szam    required
    Should Be Equal As Strings    ${vezetek_required}    true
    Should Be Equal As Strings    ${kereszt_required}    true
    Should Be Equal As Strings    ${kulcs_required}    true
    Close Browser
