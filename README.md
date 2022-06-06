## API для сервиса бронирования переговорок

Приложение предоставляет возможность бронировать помещения на определённый период времени.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AigulParamonova/room_reservation.git
```

```
cd room_reservation
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать файл .env:

```
APP_TITLE=Сервис бронирования переговорных комнат
DATABASE_URL=your_database
SECRET=your_secret
FIRST_SUPERUSER_EMAIL=your_email
FIRST_SUPERUSER_PASSWORD=your_password
```

Автогенерация миграций:

```
alembic revision --autogenerate -m "First migration"
```

Применение миграций:

```
alembic upgrade head
```

Запуск проекта:

```
uvicorn app.main:app --reload
```

Документация API:

```
http://127.0.0.1:8000/docs
```

### Технологии:
- Python 3.9
- FastAPI
- SQLAlchemy 1.4
- Git