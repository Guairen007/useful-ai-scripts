import csv
import json

csv_file = "input.csv"
json_file = "output.json"

data = []

# Read CSV rows as dictionaries
with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Save as formatted JSON
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"Converted {csv_file} to {json_file}.")