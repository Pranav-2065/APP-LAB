import csv
import json

csv_file = input("Enter CSV file name: ")
json_file = input("Enter JSON file name: ")

data = []

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append(row)

with open(json_file, "w") as file:
    json.dump(data, file, indent=4)

print("CSV file converted to JSON successfully.")
'''
c:/Users/Shriram/Desktop/SY-Advance-Python/Assignment_9/csv_to_json.py
Enter CSV file name: sample.csv
Enter JSON file name: sample.json
CSV file converted to JSON successfully.
'''
