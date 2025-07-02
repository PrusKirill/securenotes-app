# Уязвимый образ для практики
FROM python:3.12-slim

# Уязвимость 1: Работаем под root
USER root

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY . .

# Уязвимость 2: Используем дебаг-режим в продакшене
CMD ["python", "app.py", "--debug"]