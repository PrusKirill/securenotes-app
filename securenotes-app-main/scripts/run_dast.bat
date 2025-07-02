@echo off
chcp 65001 > nul
echo [1/4] Stopping any running app...
taskkill /f /im python.exe > nul 2>&1

echo [2/4] Starting application...
start "" python backend/app.py

echo [3/4] Waiting for app to start...
timeout /t 10 > nul

echo [4/4] Running DAST scan...
"C:\Program Files\ZAP\Zed Attack Proxy\zap.bat" -cmd -quickurl http://localhost:5000 -quickout ../reports/zap_report.json

echo ----------------------------
echo DAST scan completed!
echo Report: reports\zap_report.json
pause