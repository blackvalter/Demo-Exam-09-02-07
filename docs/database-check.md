# Проверка базы

1. Дождитесь healthy в docker compose ps.
2. Выполните docker compose run --rm db-check. После импорта ожидается tables=8.

При tables=0 убедитесь, что выбранная база учебная и ещё не инициализирована.
