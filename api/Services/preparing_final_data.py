import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR.parent / "final_data.json"


def getData():
    if not JSON_PATH.exists():
        print(f"CRITICAL ERROR: file not found at '{JSON_PATH}'")
        return []

    try:
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []
