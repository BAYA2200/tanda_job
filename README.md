# Kanban Project

## Описание
Это приложение для управления заказами с использованием Kanban-подхода. В проекте реализованы API для работы с заказами, аутентификация через JWT и интеграция с GraphQL.

## Установка
1. Убедитесь, что установлен Python 3.8+ и Poetry.
2. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/BAYA2200/tanda_job.git
   cd kanban_project


Установите зависимости:
poetry install
Выполните миграции:
poetry run python manage.py migrate
Запустите сервер:
poetry run python manage.py runserver