import os
import pandas as pd

# Path to your Excel file
excel_file = "names.xlsx"

# Folder where PNG files are located
png_folder = "images"

# Read the Excel file
df = pd.read_excel(excel_file)

# Clean up column names (strip newline/extra spaces)
df.columns = df.columns.str.strip()

# Loop through each row
for index, row in df.iterrows():
    num = index + 1  # Assuming row 1 → 1.png, row 2 → 2.png ...
    name = str(row["Name"]).strip()

    old_filename = os.path.join(png_folder, f"{num}.png")
    new_filename = os.path.join(png_folder, f"{name}.png")

    if os.path.exists(old_filename):
        os.rename(old_filename, new_filename)
        print(f"Renamed: {old_filename} -> {new_filename}")
    else:
        print(f"File not found: {old_filename}")
