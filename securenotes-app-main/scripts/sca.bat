@echo off
echo Создаем папку для отчетов...
mkdir reports 2> nul

echo Запуск SCA проверки...
python -m safety check -r backend/requirements.txt --output json > reports\sca_report.json

if %errorlevel% equ 0 (
    echo УСПЕХ: Отчет сохранен в reports\sca_report.json
) else (
    echo ОШИБКА: Не удалось выполнить проверку
)

pause
