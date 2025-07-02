@echo off
chcp 65001 > nul
echo [1/4] Starting application...
start "" python backend/app.py

echo [2/4] Waiting for app to start...
timeout /t 10

echo [3/4] Running DAST scan with Docker...
docker run -v %cd%\reports:/zap/reports:rw -t owasp/zap2docker-stable zap-baseline.py -t http://host.docker.internal:5000 -J zap_report.json

echo [4/4] DAST report saved to reports\zap_report.json
echo ----------------------------
pause
