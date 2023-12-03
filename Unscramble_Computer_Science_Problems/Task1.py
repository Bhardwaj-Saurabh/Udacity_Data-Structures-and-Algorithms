"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

records = []

for record in texts:
        records.append(record[0])
        records.append(record[1])

for record in calls:
        records.append(record[0])
        records.append(record[1])

counts = len(set(records))

print(f"There are {counts} different telephone numbers in the records.")
