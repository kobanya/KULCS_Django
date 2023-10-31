*** Settings ***
Library    SeleniumLibrary
Library    nevek.NevekLibrary

*** Variables ***
${URL}    http://127.0.0.1:8000/
${BROWSER}    chrome

*** Test Cases ***
Form Submission Test
    Open Browser    ${URL}    ${BROWSER}
    FOR    ${i}    IN RANGE    20
        ${first_name}    ${last_name}    ${kulcs_szam}=    Generate Random Name
        Submit Form    ${first_name}    ${last_name}  ${kulcs_szam}
    END
    Close Browser


*** Keywords ***
Submit Form
    [Arguments]    ${first_name}    ${last_name}    ${kulcs_szam}
    Input Text    id=vezetek_nev    ${last_name}
    Input Text    id=kereszt_nev    ${first_name}
    Input Text    id=kulcs_szam     ${kulcs_szam}
    Click Button    id=mentes
