Приложение на Python + Tkinter для управления каталогом товаров и заказами (демонстрационная система).

Требования
- Python 3.8+
- PostgreSQL
- Рекомендуемые пакеты (пример в requirements.txt): psycopg2-binary, pandas, openpyxl, python-dotenv, Pillow

Быстрый старт (локально)
1. Клонировать репозиторий и перейти в папку проекта.
2. Создать виртуальное окружение и активировать:
   - python -m venv .venv
   - source .venv/bin/activate  (или .venv\Scripts\activate на Windows)
3. Установить зависимости:
   - pip install -r requirements.txt

Конфигурация БД
- Настройки подключения читаются из файла [.env](.env) через [`config.DB_SETTINGS`](config.py) (см. [config.py](config.py)).
- Создать базу и таблицы:
  - Выполнить SQL-скрипт: [db_create_script.sql](db_create_script.sql)
  - Пример: psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f db_create_script.sql

Импорт тестовых данных из Excel
- Скрипт импорта: [db_pull_data.py](db_pull_data.py) который вызывает [`excels.parser.start_import`](excels/parser.py)
- Excel-файлы кладутся в папку [excels/](excels/)
- Запуск:
  - python db_pull_data.py
- Код импорта: [excels/parser.py](excels/parser.py)

Структура репозитория (важные файлы)
- [main.py](main.py)
- [config.py](config.py) — переменные окружения и пути, [`config.DB_SETTINGS`](config.py)
- [database.py](database.py) — слой доступа к БД
- [db_create_script.sql](db_create_script.sql) — схема БД
- [db_pull_data.py](db_pull_data.py) и [excels/parser.py](excels/parser.py) — импорт из Excel
- UI: [ui/](ui/) — [`ui.login_window.LoginWindow`](ui/login_window.py), [`ui.main_app_window.MainAppWindow`](ui/main_app_window.py), редакторы товаров/заказов