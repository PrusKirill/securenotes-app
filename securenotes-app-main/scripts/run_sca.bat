@echo off
chcp 65001 > nul
echo [1/3] Activating virtual environment...
call .\.venv\Scripts\activate

echo [2/3] Running SCA check...
python -m safety check -r backend/requirements.txt --output json > reports\sca_report.json

if %errorlevel% equ 0 (
    echo [3/3] SUCCESS: Report saved to reports\sca_report.json
) else (
    echo [ERROR] SCA check failed
)

echo ----------------------------
echo Press any key to exit...
pause > nul