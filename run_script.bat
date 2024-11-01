@echo off
REM Run pytest
pytest

REM Serve Allure report
start cmd /k "allure serve .\reports\allure-results"

REM Open coverage html report
start .\reports\coverage_report_html\index.html


