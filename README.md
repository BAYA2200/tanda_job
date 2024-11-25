# Kanban Project

## 📋 Описание
**Kanban Project** — это приложение для управления заказами с использованием подхода Kanban.  
Проект включает следующие ключевые функции:
- Обработка заказов через GraphQL API.
- Управление статусами заказов.
- JWT-аутентификация для пользователей.
- Интерактивный интерфейс для работы с API (`GraphiQL`, Swagger и Redoc).

## 🚀 Функционал
1. **Пользователи**:
   - Регистрация новых пользователей.
   - Авторизация с помощью JWT.
   - Получение данных о текущем пользователе.

2. **Управление заказами**:
   - Создание, просмотр и изменение заказов.
   - Поддержка смены статуса заказов (Kanban-подход).

3. **Документация API**:
   - Swagger для REST API.
   - GraphiQL для тестирования GraphQL-запросов.

---

## 🛠️ Установка

### Требования
- Python 3.8+
- [Poetry](https://python-poetry.org/docs/#installation)

### Инструкции

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/BAYA2200/tanda_job.git
   cd kanban_project
   ```

2. **Установка зависимостей**:
   ```bash
   poetry install
   ```

3. **Применение миграций**:
   ```bash
   poetry run python manage.py migrate
   ```

4. **Запуск локального сервера**:
   ```bash
   poetry run python manage.py runserver
   ```
   Сервер будет доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 📄 Использование

### Endpoints
- **GraphQL API**:  
  URL: [http://127.0.0.1:8000/graphql/](http://127.0.0.1:8000/graphql/)  
  Используйте GraphiQL или Postman для отправки запросов.

- **Swagger UI**:  
  URL: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

- **Redoc**:  
  URL: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

### Примеры запросов GraphQL

#### 1. Запрос текущего пользователя:
```graphql
query {
  me {
    id
    username
    email
  }
}
```

#### 2. Создание нового заказа:
```graphql
mutation {
  createOrder(title: "New Order", description: "Details of the order.") {
    order {
      id
      title
      description
      status
    }
  }
}
```

#### 3. Обновление статуса заказа:
```graphql
mutation {
  updateOrderStatus(id: 1, status: "completed") {
    order {
      id
      status
    }
  }
}
```

---

## 🧪 Тестирование

Для выполнения тестов:
```bash
poetry run pytest
```

---

## 🌐 Деплой
### Возможные сервисы:
1. [Heroku](https://www.heroku.com/)
2. [Railway](https://railway.app/)
3. [Render](https://render.com/)

### Шаги деплоя:
1. Создайте `.env` файл с настройками окружения.
2. Настройте базу данных (например, PostgreSQL).
3. Загрузите проект на сервер и выполните миграции:
   ```bash
   poetry run python manage.py migrate
   ```
4. Запустите сервер.

---

## 👨‍💻 Контакты
Для вопросов и предложений:  
**Email:** support@example.com  
**GitHub:** [https://github.com/BAYA2200/tanda_job](https://github.com/BAYA2200/tanda_job)

--- 

### 📌 Примечание
**Kanban Project** разработан с упором на производительность и гибкость. Поддерживаются как REST API, так и GraphQL, чтобы соответствовать современным требованиям разработки.