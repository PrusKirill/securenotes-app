@echo off
chcp 65001 > nul
echo [1/3] Running Dockerfile scan...
checkov -f backend/Dockerfile --output json --output-file-path reports/ --skip-download

if %errorlevel% equ 0 (
    echo [2/3] SUCCESS: Report saved to reports\checkov_report.json
) else (
    echo [ERROR] Dockerfile scan failed
)

echo [3/3] Found issues:
python -c "import json; report = json.load(open('reports\\checkov_report.json')); [print(f'- {check['check_id']}: {check['check_name']}') for check in report['results']['failed_checks']]"

echo ----------------------------
echo Press any key to exit...
pause > nul
