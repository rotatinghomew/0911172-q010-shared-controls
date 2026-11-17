import json
from pathlib import Path

def build_report(title, group_key, value_key, records, summary):
    return {"title": title, "group": group_key, "measure": value_key,
            "record_count": len(records), "summary": summary}

def write_report(report, path):
    Path(path).write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
