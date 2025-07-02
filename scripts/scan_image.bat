@echo off
chcp 65001 > nul
echo [1/3] Running image scan...
trivy\trivy.exe image --format json --output reports/trivy_report.json securenotes-app:latest

if %errorlevel% equ 0 (
    echo [2/3] SUCCESS: Report saved to reports\trivy_report.json
) else (
    echo [ERROR] Image scan failed
)

echo [3/3] Found HIGH/CRITICAL vulnerabilities:
python -c "import json; report = json.load(open('reports\\trivy_report.json')); [print(f'- {vuln['VulnerabilityID']}: {vuln['Title']} (Severity: {vuln['Severity']})') for result in report['Results'] for vuln in result.get('Vulnerabilities', []) if vuln['Severity'] in ['HIGH', 'CRITICAL']]"

echo ----------------------------
echo Press any key to exit...
pause > nul