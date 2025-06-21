@echo off
echo 🔁 Starting Vernacular AI Assistant...

REM 1. Activate your virtual environment if needed
REM call venv\Scripts\activate

REM 2. Start Flask server in the background
start cmd /k python app.py

REM 3. Wait for Flask to start
timeout /t 2 /nobreak >nul

REM 4. Open the web interface
start http://127.0.0.1:5000

exit
