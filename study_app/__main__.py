import argparse
import json
from pathlib import Path
from .analysis import summarize
from .ingest import load_records
from .report import build_report, write_report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/sample.json")
    parser.add_argument("--output", default="report.json")
    args = parser.parse_args()
    config = json.loads(Path("project.json").read_text(encoding="utf-8"))
    records = load_records(args.data)
    summary = summarize(records, config["group_key"], config["value_key"])
    report = build_report(config["title"], config["group_key"], config["value_key"], records, summary)
    write_report(report, args.output)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))

if __name__ == "__main__":
    main()
