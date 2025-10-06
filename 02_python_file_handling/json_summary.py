# ======================================================
# File: json_summary.py
# Topic: Summarizing JSON data (average salary per role)
# ======================================================
# This script demonstrates:
# 1) Reading a JSON file into Python (list of dicts).
# 2) Grouping data by a categorical key (role).
# 3) Computing the average of numeric fields (salary).
# 4) Printing a clean summary.
# ======================================================

import os
import json
from collections import defaultdict  # helps group by keys easily

# ------------------------------
# STEP 1: Build input path
# ------------------------------
HERE = os.path.dirname(__file__)
IN = os.path.join(HERE, "processed", "employees_processed.json")

# ------------------------------
# STEP 2: Load JSON file
# ------------------------------
with open(IN, "r", encoding="utf-8") as f:
    data = json.load(f)  # list of dictionaries
print(f"Loaded {len(data)} records from {IN}")

# ------------------------------
# STEP 3: Group by 'role' and compute average salary
# ------------------------------
# defaultdict creates a dictionary where each key starts as an empty list.
salaries_by_role = defaultdict(list)

for row in data:
    role = row.get("role", "Unknown")
    try:
        salary = float(row.get("salary", 0))
    except ValueError:
        salary = 0.0
    salaries_by_role[role].append(salary)

# Compute averages
avg_by_role = {}
for role, salaries in salaries_by_role.items():
    avg = sum(salaries) / len(salaries) if salaries else 0
    avg_by_role[role] = round(avg, 2)

# ------------------------------
# STEP 4: Display summary
# ------------------------------
print("\nAverage salary by role:")
for role, avg in avg_by_role.items():
    print(f"  {role:<15} → ₹ {avg:,.2f}")
