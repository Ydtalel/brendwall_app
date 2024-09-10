# Product API

Простое веб-приложение для управления продуктами, реализованное с использованием Django и Django REST Framework (DRF). Приложение предоставляет API для добавления и просмотра продуктов.

## Клонирование проекта

Сначала клонируйте репозиторий на локальную машину:

```bash
git clone https://github.com/Ydtalel/brendwall_app.git
```
### Запуск с помощью Docker

1. Сборка образа:  

    `make build`

2. Запуск контейнера:

    `make run`
3. Применение миграции:

   `make migrate`

Приложение будет доступно по адресу:   

`http://localhost:8000/web/products/`

4. Остановка контейнера:

   `make stop`

### Запуск без Docker

1. Установка зависимостей:  
Создайте виртуальное окружение и установите зависимости:  
`python -m venv venv`  
source venv/bin/activate   
Для Windows: venv\Scripts\activate  
pip install -r requirements.txt


2. Применение миграций:  

   `python manage.py makemigrations products`  

   `python manage.py migrate`


3. Запуск сервера разработки:  

   `python manage.py runserver`  

Приложение будет доступно по адресу:  

`http://localhost:8000/web/products/`

### Swagger UI:
Если вы запускаете сервер разработки без Docker,  
интерфейс Swagger будет доступен по адресу:  
`http://localhost:8000/swagger/`

### Операции API
1. Добавление продукта  
POST `http://127.0.0.1:8000/api/products/`

Пример тела запроса:
```
{
  "name": "Example Product",
  "price": 100.0,
  "description": "A sample product description."
}
```
2. Получение списка продуктов  
GET `http://127.0.0.1:8000/api/products/`


3. Получение информации о продукте  
GET `http://127.0.0.1:8000/api/products/{id}/`
