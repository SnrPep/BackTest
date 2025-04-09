FROM python:3.9-slim

# Создаём рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект
COPY DDS .

# Команда запуска по умолчанию
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]