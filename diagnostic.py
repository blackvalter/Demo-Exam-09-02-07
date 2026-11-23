from pathlib import Path
import json
import sys
import tkinter as tk

import config
import database

def run_diagnostic(path):
    result = {
        "frozen": bool(getattr(sys, "frozen", False)),
        "logo": Path(config.LOGO_PATH).is_file(),
        "icon": Path(config.ICON_PATH).is_file(),
        "placeholder": Path(config.PLACEHOLDER_IMAGE_PATH).is_file(),
    }
    app = tk.Tk()
    app.withdraw()
    try:
        result["tk"] = app.tk.call("info", "patchlevel")
        conn = database.get_connection()
        result["database"] = conn is not None
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT count(*) FROM products")
                    result["products"] = cursor.fetchone()[0]
            finally:
                conn.close()
    except Exception as error:
        result["error"] = type(error).__name__
    finally:
        app.destroy()
    Path(path).write_text(json.dumps(result, indent=2), encoding="utf-8")
    return 0 if all(result.get(key) for key in ("logo", "icon", "placeholder", "database")) and "products" in result else 1

