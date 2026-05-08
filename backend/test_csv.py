import os
import pandas as pd

csv_path = "data/resume_job_description.csv"

print("Checking file path:", csv_path)

if not os.path.exists(csv_path):
    print("File not found. Check your CSV name inside data folder.")
else:
    print("File exists.")

    if os.path.isdir(csv_path):
        print("Problem: This path is a folder, not a CSV file.")
    else:
        df = pd.read_csv(csv_path)

        print("First 5 rows:")
        print(df.head())

        print("\nColumn names:")
        print(df.columns.tolist())

        print("\nDataset shape:")
        print(df.shape)