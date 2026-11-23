"""Run from anywhere with: python 05_tests/01_test_pipeline.py"""
from pathlib import Path
import csv
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PipelineTest(unittest.TestCase):
    def test_example_reproduces_prediction(self):
        for step in ("01_validate_data.py", "02_score_guests.py", "03_create_report.py"):
            subprocess.run(
                [sys.executable, str(ROOT / "02_scripts" / step)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
        with (ROOT / "03_outputs" / "01_sleepiness_scores.csv").open(newline="", encoding="utf-8") as handle:
            scores = list(csv.DictReader(handle))
        self.assertEqual(len(scores), 6)
        top = max(scores, key=lambda row: float(row["sleepiness_score"]))
        self.assertEqual(top["name"], "Aunt May")
        report = (ROOT / "03_outputs" / "02_prediction.md").read_text(encoding="utf-8")
        self.assertIn("**Predicted first to fall asleep: Aunt May**", report)

if __name__ == "__main__":
    unittest.main()
