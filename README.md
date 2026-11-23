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

## Учебный стенд практик 11–14

Ветка practicum/11-14 содержит конфигурацию Compose, учебные данные,
проверки каталога и сценарий сборки Windows. Исходный клиент использует
Tkinter. Контейнеры запускают PostgreSQL и вспомогательную проверку.

### Чистая БД и клиент

1. Скопируйте .env.example в .env рядом с main.py. Укажите свой пароль учебной БД.
2. Выполните docker compose up -d --wait db.
3. Для пустой базы скопируйте db_create_script.sql и lab/seed.sql в контейнер
   командами docker compose cp и выполните их через psql с ON_ERROR_STOP=1.
   Первый скрипт пересоздаёт таблицы, а второй добавляет синтетические записи.
   Используйте их только на отдельной учебной базе.
4. Выполните docker compose run --rm db-check. После импорта ожидается tables=8.
5. Установите зависимости в отдельном окружении и откройте python main.py.
   Учебная учётная запись приложения lab_admin, пароль demo-only-admin
   предназначены только для синтетической локальной базы.

Постоянное хранилище включается дополнительным файлом
compose.persistence.yaml. Сначала сделайте pg_dump, затем подключите
именованный том и восстановите копию в пустую БД через pg_restore.
Для клиентского приложения используйте 127.0.0.1:5433, для db-check — db:5432.
Порядок проверок приведён в [заметке по БД](docs/database-check.md).

### Проверки и Windows-сборка

Из корня запускайте python -m unittest discover -s tests -v.
Установите PyInstaller и запустите build-win.ps1 на Windows.
После сборки копируйте папку dist/ShoeStore целиком. Файл .env лежит
рядом с ShoeStore.exe, а комплект ресурсов уже включён в сборку.
Ключ --diagnose с путём к отчёту проверяет Tk, наличие ресурсов,
подключение и число товаров без вывода реквизитов.

