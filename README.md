# Wiki
Project1 from cs50 course

## Docker
Сборка всех образов и запуск

`docker-compose up -d --build`

Произвести миграции

`docker-compose exec web python manage.py migrate --noinput`

## Ссылка на страницу сервиса

`http://localhost:8000/`
