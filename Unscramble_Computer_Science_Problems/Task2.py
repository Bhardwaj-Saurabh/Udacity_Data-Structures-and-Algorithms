"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_duration = {}

for record in calls:
    if record[0] not in call_duration.keys():
        call_duration[record[0]] = float(record[-1])
    else:
        call_duration[record[0]] += float(record[-1])


    if record[1] not in call_duration.keys():
        call_duration[record[1]] = float(record[-1])
    else:
        call_duration[record[1]] += float(record[-1])


for key, value in call_duration.items():
    if value == max(call_duration.values()):
        print(f"{key} spent the longest time, {value} \
seconds, on the phone during September 2016.")