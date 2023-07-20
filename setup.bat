@echo off

:start
cls

py -m venv venv && call .\venv\Scripts\activate && pip install -r requirements.txt

pause
exit