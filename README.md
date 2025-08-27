# Artists & Albums API

Каталог исполнителей, альбомов и песен.  
Одна и та же песня может входить в разные альбомы (с разными порядковыми номерами в каждом альбоме).


## Стек
- Python 3.9+
- Django 4.x
- Django REST Framework
- drf-spectacular (Swagger UI для документации)

### Клонирование репозитория
```bash
git clone git@github.com:boltnevasof/Artists_albums.git
cd Artists_albums
```
Создайте и активируйте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # для macOS
```

Установите зависимости:
```
pip install -r requirements.txt
```
## Миграции и суперпользователь
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
# Запуск сервера
```
python manage.py runserver
```
```
Админка: http://127.0.0.1:8000/admin/

API root: http://127.0.0.1:8000/api/

Swagger UI: http://127.0.0.1:8000/api/docs/

OpenAPI JSON: http://127.0.0.1:8000/api/schema/
```
## Структура данных (модели)
```
Artist: name — исполнитель
Song: name — песня
Album: artist (FK), title, release_year, songs (M2M через AlbumTrack)
AlbumTrack: album (FK), song (FK), track_number
```
# Ограничения на уровне базы данных:
```
(album, song) — песня не может повторяться в одном альбоме

(album, track_number) — номер трека уникален внутри альбома
```
## Эндпоинты API
```
GET/POST /api/artists/ — список исполнителей / создание
GET/PUT/PATCH/DELETE /api/artists/{id}/ — операции с конкретным исполнителем
GET/POST /api/songs/ — список песен / создание
GET/PUT/PATCH/DELETE /api/songs/{id}/ — операции с конкретной песней
GET/POST /api/albums/ — список альбомов / создание
GET/PUT/PATCH/DELETE /api/albums/{id}/ — операции с конкретным альбомом
GET/POST /api/tracks/ — список треков / создание
GET/PUT/PATCH/DELETE /api/tracks/{id}/ — операции с конкретным треком
```
## Примеры запросов

# Создать исполнителя:
```
curl -X POST http://127.0.0.1:8000/api/artists/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Massive Attack"}'
```

# Создать песню:
```
curl -X POST http://127.0.0.1:8000/api/songs/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Teardrop"}'
```

# Создать альбом:
```
curl -X POST http://127.0.0.1:8000/api/albums/ \
  -H "Content-Type: application/json" \
  -d '{"artist":1, "title":"Mezzanine", "release_year":1998}'
```

# Добавить песню в альбом:
```
curl -X POST http://127.0.0.1:8000/api/tracks/ \
  -H "Content-Type: application/json" \
  -d '{"album":1,"song":1,"track_number":2}'
```
# Swagger / Postman
```
Swagger UI: /api/docs/

OpenAPI JSON: /api/schema/ (можно импортировать в Postman)
```