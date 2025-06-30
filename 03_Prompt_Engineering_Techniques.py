# 3. Act as a Python developer. Write code to read and print duplicate records from the provided CSV file, remove it from the old csv file and give the updated csv file

import pandas as pd
import os
import csv

file_name = input("Enter the name of the CSV file (with .csv extension): ")

if not os.path.isfile(file_name):
    print(f"The file {file_name} does not exist.")
else:
    df = pd.read_csv(file_name)

    duplicates = df[df.duplicated(keep=False)]

    print("Duplicate records are:")
    print(duplicates)

    df = df.drop_duplicates()

    # get teh extension form the File
    file_name, file_extension = os.path.splitext(file_name)

    updated_file_name = file_name + "duplicate_removed_"
    updated_file_name += file_extension

    df.to_csv(updated_file_name, index=False)
    print(f"Updated CSV file saved as {updated_file_name}")
