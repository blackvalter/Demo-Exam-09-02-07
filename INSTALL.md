# Установка и запуск ShoeStore

Требуются Windows 10/11 x64, Docker Desktop с Linux containers и Compose v2.
Клиент распространяется в формате onedir. Переносите каталог ShoeStore целиком,
включая _internal. Python и IDE для готового EXE не требуются.

## Подготовка инфраструктуры

Распакуйте ZIP в доступный для записи каталог. Откройте PowerShell в deployment.

~~~powershell
Copy-Item .env.example .env
notepad .env
docker compose -f compose.yaml -f compose.persistence.yaml up -d --wait db
~~~

В .env укажите пароль новой учебной БД. Эти переменные задают настройки только
при первичной инициализации PostgreSQL в пустом томе. Изменение файла для
существующего тома само по себе пароль роли не меняет.

Для новой пустой учебной БД скопируйте SQL в контейнер, затем примените скрипты.

~~~powershell
docker compose -f compose.yaml -f compose.persistence.yaml cp db_create_script.sql db:/tmp/shoe-schema.sql
docker compose -f compose.yaml -f compose.persistence.yaml cp seed.sql db:/tmp/shoe-seed.sql
docker compose -f compose.yaml -f compose.persistence.yaml exec db psql -v ON_ERROR_STOP=1 -U shoe_lab -d shoe_store -f /tmp/shoe-schema.sql
docker compose -f compose.yaml -f compose.persistence.yaml exec db psql -v ON_ERROR_STOP=1 -U shoe_lab -d shoe_store -f /tmp/shoe-seed.sql
docker compose -f compose.yaml -f compose.persistence.yaml run --build --rm db-check
~~~

Команды используют имя базы и роль из образца. Если вы меняли их, подставьте
свои значения. После импорта ожидается OK: connected, tables=8.
Скрипт первоначальной схемы пересоздаёт таблицы. Для существующей базы с данными
пропустите оба импорта.

## Конфигурация и запуск клиента

Скопируйте deployment/.env в application/ShoeStore/.env. Для клиента Windows
используйте DB_HOST=127.0.0.1 и DB_PORT=5433. Дополнительный config.ini
в этом проекте не используется. Запустите application/ShoeStore/ShoeStore.exe.
Для синтетического стенда доступны гостевой режим и учебная учётная запись
lab_admin с демонстрационным паролем demo-only-admin, указанным в seed.sql.

Проверка из любой рабочей папки с PowerShell:

~~~powershell
Start-Process -FilePath 'C:\путь\ShoeStore.exe' -ArgumentList '--diagnose','shoe-diagnostic.json' -Wait -PassThru
~~~

Код 0 означает, что загрузился Tk, доступны ресурсы, выполнено подключение и
читается каталог. Поле products содержит число записей. Код 1 означает
невыполненное условие. Пароль в диагностический JSON не включается.

## Остановка и диагностика

Остановите контейнеры командой docker compose -f compose.yaml
-f compose.persistence.yaml stop. Именованный том сохранится.
При пустом каталоге запустите db-check и убедитесь, что имя БД совпадает.
Если 5433 занят, выберите свободный порт и согласованно измените DB_PORT
в конфигурации инфраструктуры и Windows-клиента. Подключение из db-check
по-прежнему использует db:5432.

