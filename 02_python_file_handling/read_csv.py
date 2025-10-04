# ======================================================
# STEP 1: Build the file path dynamically
# ------------------------------------------------------
# __file__ : special Python variable → full path to this script.
# os.path.dirname(__file__) → gives only the directory part (folder).
# os.path.join(base_path, "sample.csv") → adds the CSV file name
#                                         to the folder path safely.
# This ensures that Python can find the CSV file
# even if you run the script from another directory.
# ======================================================


import os
import csv

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "sample.csv")

# STEP 2: Open the CSV file safely using 'with' (auto-closes file)
with open(file_path, "r") as file:
    reader = csv.reader(file)
    
    # STEP 3: Loop through rows and print them
    for row in reader:
        print(row)


