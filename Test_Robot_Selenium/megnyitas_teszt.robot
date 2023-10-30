*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${SERVER}         http://127.0.0.1:8000
${BROWSER}        Chrome

*** Test Cases ***
Open Django Homepage
    Open Browser    ${SERVER}    ${BROWSER}
    Title Should Be    Kulcs nyilvántartás
    Close Browser
