import json
from pathlib import Path

def load_records(path):
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    rows = payload["records"]
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError("records must be a list of objects")
    return rows
