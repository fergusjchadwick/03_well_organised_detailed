"""Stage 2: calculate a deliberately arbitrary festive sleepiness score."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "01_data" / "02_validated_guests.csv"
DEST = ROOT / "03_outputs" / "01_sleepiness_scores.csv"

with SOURCE.open(newline="", encoding="utf-8") as handle:
    guests = list(csv.DictReader(handle))

DEST.parent.mkdir(parents=True, exist_ok=True)
with DEST.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["name", "sleepiness_score"])
    writer.writeheader()
    for guest in guests:
        score = (
            2 * float(guest["travel_hours"])
            + 1.5 * float(guest["dinner_portions"])
            + 0.02 * float(guest["age_years"])
            - 1.8 * float(guest["coffees"])
        )
        writer.writerow({"name": guest["name"], "sleepiness_score": f"{score:.2f}"})
print(f"Scored {len(guests)} guests -> {DEST.relative_to(ROOT)}")
