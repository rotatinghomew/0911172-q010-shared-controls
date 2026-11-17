import json
import tempfile
import unittest
from pathlib import Path
from study_app.analysis import summarize
from study_app.ingest import load_records
from study_app.report import build_report, write_report

class AnalysisFlowTests(unittest.TestCase):
    def test_sample_flows_from_records_into_auditable_report(self):
        root = Path(__file__).resolve().parents[1]
        config = json.loads((root / "project.json").read_text(encoding="utf-8"))
        records = load_records(root / "data" / "sample.json")
        summary = summarize(records, config["group_key"], config["value_key"])
        result = build_report(config["title"], config["group_key"], config["value_key"], records, summary)
        self.assertEqual(result["record_count"], len(records))
        self.assertTrue(result["summary"])
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "report.json"
            write_report(result, target)
            self.assertEqual(json.loads(target.read_text(encoding="utf-8")), result)

    def test_missing_measurement_does_not_enter_numeric_denominator(self):
        result = summarize([{"g": "a", "v": 1}, {"g": "a", "v": None}], "g", "v")
        self.assertEqual(result["a"], {"n": 1, "mean": 1.0})

if __name__ == "__main__":
    unittest.main()
