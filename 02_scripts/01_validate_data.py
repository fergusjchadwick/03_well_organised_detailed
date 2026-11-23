"""Stage 1: validate the fictional input data without third-party packages."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "01_data" / "01_christmas_guests.csv"
DEST = ROOT / "01_data" / "02_validated_guests.csv"
COLUMNS = ["name", "age_years", "travel_hours", "dinner_portions", "coffees"]

with SOURCE.open(newline="", encoding="utf-8") as handle:
    reader = csv.DictReader(handle)
    if reader.fieldnames != COLUMNS:
        raise ValueError(f"Expected columns {COLUMNS}; received {reader.fieldnames}")
    rows = list(reader)

if not rows:
    raise ValueError("At least one guest is required")
if len({row["name"] for row in rows}) != len(rows):
    raise ValueError("Guest names must be unique")
for row in rows:
    if not row["name"].strip():
        raise ValueError("Guest names cannot be empty")
    for key in COLUMNS[1:]:
        try:
            value = float(row[key])
        except (ValueError, TypeError) as exc:
            raise ValueError(f"Invalid {key} for {row['name']}") from exc
        if not 0 <= value < float("inf"):
            raise ValueError(f"{key} must be finite and nonnegative")

with DEST.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)
print(f"Validated {len(rows)} guests -> {DEST.relative_to(ROOT)}")
