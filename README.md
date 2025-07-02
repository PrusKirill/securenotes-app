[![Security Scans](https://github.com/ваш-логин/securenotes-app/actions/workflows/security-scans.yml/badge.svg)](https://github.com/ваш-логин/securenotes-app/actions)
# SecureNotes - Educational Security Project

![Python](https://img.shields.io/badge/python-3.12-blue)
![Flask](https://img.shields.io/badge/flask-2.3-green)

Web application with intentionally implemented vulnerabilities for security testing practice.

## Features
- SQL Injection
- Cross-Site Scripting (XSS)
- Insecure Deserialization
- Path Traversal
- Sensitive Data Exposure

## Security Tools
- Pre-commit hooks
- SCA: Safety
- SAST: Bandit
- Docker: Checkov, Trivy
- DAST: OWASP ZAP

## How to Run
```bash
cd backend
pip install -r requirements.txt
python app.py
## Security Scans
We use automated security checks:

[![SCA](https://github.com/PrusKirill/securenotes-app/actions/workflows/security-scans.yml/badge.svg)](https://github.com/PrusKirill/securenotes-app/actions)
