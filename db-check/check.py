"""Check the database and report the schema table count."""
import os
import sys
import psycopg

def main():
    try:
        with psycopg.connect(
            host=os.environ["DB_HOST"], port=os.environ["DB_PORT"],
            dbname=os.environ["DB_NAME"], user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"], connect_timeout=5,
        ) as conn:
            tables, = conn.execute(
                "SELECT count(*) FROM information_schema.tables "
                "WHERE table_schema = 'public' AND table_type = 'BASE TABLE'"
            ).fetchone()
        print(f"OK: connected, tables={tables}")
        return 0
    except (KeyError, psycopg.Error) as error:
        print(f"DB check failed: {type(error).__name__}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
