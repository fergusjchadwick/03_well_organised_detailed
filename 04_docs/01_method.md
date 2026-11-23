# Method and data dictionary

This repository is a *documentation teaching example*, not an empirical model of sleep.
The example contains only fictional guests and invented measurements.

## Data

`01_data/01_christmas_guests.csv` contains one row per guest:

| Variable | Meaning | Unit |
| --- | --- | --- |
| `name` | Fictional guest identifier | Text |
| `age_years` | Guest's age | Years |
| `travel_hours` | Duration of their trip to Christmas lunch | Hours |
| `dinner_portions` | Number of portions eaten | Portions |
| `coffees` | Number of caffeinated coffees | Drinks |

The validation stage checks the header, unique nonempty guest names, and finite,
nonnegative numeric values. It does **not** check that input values are plausible.

## Arbitrary scoring rule

```text
sleepiness_score = 2 × travel_hours
                 + 1.5 × dinner_portions
                 + 0.02 × age_years
                 - 1.8 × coffees
```

Higher scores rank earlier, with alphabetical ordering to break exact ties.
The coefficients have not been estimated from data or scientifically validated.

## Reproducibility

The three scripts use only the Python standard library and resolve paths relative
to this repository, not the shell's current working directory. Running them in
sequence overwrites the example validated data and output files deterministically.
The small generated files are intentionally committed so visitors can inspect
results without running the code. In larger projects, these may instead be excluded
from version control, depending on reproducibility requirements.
