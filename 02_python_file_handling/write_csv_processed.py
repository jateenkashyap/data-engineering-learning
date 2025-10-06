# ======================================================
# File: write_csv_processed.py
# Topic: Transforming rows and writing a processed CSV
# ======================================================
# What this script does:
# 1) Reads rows from sample.csv using DictReader.
# 2) Adds two derived columns per row:
#       - annual_bonus  = salary * BONUS_RATE (rounded to 2 decimals)
#       - is_high_earner = True/False based on a threshold
# 3) Writes the result to processed/employees_processed.csv using DictWriter.
# 4) Prints a small preview + a success message with row count.
# ======================================================

import os
import csv

# ------------------------------
# Config / "business rules"
# ------------------------------
BONUS_RATE = 0.10      # 10% annual bonus
HIGH_EARNER_THRESHOLD = 90000  # tweak this if you like

# ------------------------------
# Paths
# ------------------------------
HERE = os.path.dirname(__file__)                       # folder of this script
IN = os.path.join(HERE, "sample.csv")                  # input CSV
OUT_DIR = os.path.join(HERE, "processed")              # output folder
OUT = os.path.join(OUT_DIR, "employees_processed.csv") # output CSV

# Ensure output directory exists (safe if already there)
os.makedirs(OUT_DIR, exist_ok=True)

# ------------------------------
# Helpers
# ------------------------------
def parse_salary(value: str) -> float:
    """
    Turn a salary string into a float safely.
    Handles empty strings; strips commas if present.
    """
    if value is None:
        return 0.0
    s = value.replace(",", "").strip()
    return float(s) if s else 0.0

# ------------------------------
# Read → Transform → Write
# ------------------------------
with open(IN, newline="", encoding="utf-8") as f_in:
    reader = csv.DictReader(f_in)

    # Prepare output header: original columns + our new fields.
    out_fieldnames = list(reader.fieldnames or []) + ["annual_bonus", "is_high_earner"]

    with open(OUT, "w", newline="", encoding="utf-8") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=out_fieldnames)
        writer.writeheader()

        row_count = 0
        preview = []

        for row in reader:
            # Parse numeric salary
            salary = parse_salary(row.get("salary"))

            # Compute derived columns
            annual_bonus = round(salary * BONUS_RATE, 2)
            is_high_earner = salary > HIGH_EARNER_THRESHOLD

            # Attach new columns to the row dict
            row["annual_bonus"] = annual_bonus
            row["is_high_earner"] = is_high_earner

            writer.writerow(row)
            row_count += 1

            # Save a couple rows to preview later
            if len(preview) < 2:
                preview.append(dict(row))  # copy for printing

# ------------------------------
# Post-run feedback
# ------------------------------
print(f"Wrote: {OUT}")
print(f"Rows written: {row_count}")
print("Preview of first 2 rows with derived columns:")
for r in preview:
    print(r)
