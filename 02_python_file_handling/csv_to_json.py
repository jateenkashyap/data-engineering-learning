# ======================================================
# File: csv_to_json.py
# Topic: Converting a processed CSV to JSON format
# ======================================================
# What this script does:
# 1) Reads the processed CSV file (employees_processed.csv).
# 2) Converts each row into a Python dictionary.
# 3) Writes all rows as a JSON array to employees_processed.json.
# 4) Pretty-prints (indented) for human readability.
# ======================================================

import os
import csv
import json  # built-in module for JSON handling

# ------------------------------
# Paths
# ------------------------------
HERE = os.path.dirname(__file__)
IN = os.path.join(HERE, "processed", "employees_processed.csv")
OUT = os.path.join(HERE, "processed", "employees_processed.json")

# ------------------------------
# Read CSV into list of dicts
# ------------------------------
with open(IN, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)  # list of dictionaries

# ------------------------------
# Write JSON
# ------------------------------
with open(OUT, "w", encoding="utf-8") as f:
    # json.dump() writes data to a file
    # indent=4 → pretty format with spaces
    # ensure_ascii=False → keeps special characters readable
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ JSON file created successfully: {OUT}")
print(f"Total records exported: {len(data)}")
