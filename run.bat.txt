@echo off
call venv\scripts\activate
pytest -v -s -m "regression" --html  .\reports\report.html --browser chrome
pause