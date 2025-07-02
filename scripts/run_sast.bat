@echo off
chcp 65001 > nul
echo [1/3] Activating virtual environment...
call .\.venv\Scripts\activate

echo [2/3] Running SAST check...
python -m bandit -r backend/ -f json -o reports\bandit_report.json

if %errorlevel% equ 0 (
    echo [3/3] SUCCESS: Report saved to reports\bandit_report.json
    echo Found vulnerabilities:
    python -c "import json; report = json.load(open('reports\\bandit_report.json')); [print(f'- {r['test_name']} in {r['filename']}:{r['line_number']}') for r in report['results']]"
) else (
    echo [ERROR] SAST check failed
)

echo ----------------------------
echo Press any key to exit...
pause > nul