# 1. Создаём виртуальное окружение:
   - python3 -m venv venv
   - source venv/bin/activate

# 2. Устанавливаем библиотеки:
   - pip install -r requirements.txt

# 3. Создаём БД через docker-compose:
   - docker-compose up -d

# 4. Делаем Миграции:
   - flask -A app:app db init
   - flask db migrate -m 'makemigrations'
   - flask db upgrade

# 5. Запускаем приложение:
   - gunicorn -b 0.0.0.0:8000 app:app

# Создаем запросы через файл (requests.http)
