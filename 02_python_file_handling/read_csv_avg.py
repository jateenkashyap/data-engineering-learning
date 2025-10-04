"""
------------------------------------------------------------
File: read_csv_avg.py
Topic: Reading and Processing CSV Data in Python
------------------------------------------------------------
This script demonstrates:
1. How to locate and open a CSV file.
2. How to skip the header row.
3. How to extract specific columns (like salary).
4. How to calculate an average value using Python.
------------------------------------------------------------
"""

import os
import csv

# ======================================================
# STEP 1: Build the file path dynamically
# ------------------------------------------------------
# __file__ → the full path of the current Python script.
# os.path.dirname(__file__) → gives the folder where the script lives.
# os.path.join() → joins that folder with "sample.csv" safely.
# This makes sure Python always finds the file even if the script
# is run from another location.
# ======================================================

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "sample.csv")

# ======================================================
# STEP 2: Open and read the CSV file safely
# ------------------------------------------------------
# Using "with open(...)" automatically closes the file
# after the indented block finishes.
# csv.reader() reads the CSV line by line, splitting by commas.
# ======================================================

with open(file_path, "r") as file:
    reader = csv.reader(file)
    
    # Convert the reader object to a list so we can reuse it
    rows = list(reader)

# ======================================================
# STEP 3: Separate header and data rows
# ------------------------------------------------------
# The first row of most CSVs is a header (column names),
# e.g. ['id', 'name', 'role', 'salary']
# We can slice it off easily using indexing.
# ======================================================

header = rows[0]
data_rows = rows[1:]

print("Header:", header)
print("\nData Rows:")
for row in data_rows:
    print(row)

# ======================================================
# STEP 4: Extract and convert the salary column
# ------------------------------------------------------
# Each row looks like ['1', 'Alice', 'Data Engineer', '75000']
# The salary is the 4th item (index 3).
# We convert it to int (or float) for math operations.
# ======================================================

salaries = [float(row[3]) for row in data_rows]
print("\nSalaries:", salaries)

# ======================================================
# STEP 5: Calculate the average salary
# ------------------------------------------------------
# We use Python’s built-in sum() and len() to compute the mean.
# ======================================================

average_salary = sum(salaries) / len(salaries)
print("\nAverage Salary:", round(average_salary, 2))
