@echo off
REM Run pytest
pytest

REM Open coverage html report
start .\reports\coverage_report\index.html

REM Serve Allure report
start cmd /k "allure serve .\reports\allure-results"




