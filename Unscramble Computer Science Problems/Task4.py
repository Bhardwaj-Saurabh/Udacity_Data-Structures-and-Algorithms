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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

caller_calls = [record[0] for record in calls if record[0][:3] == '140']
reciever_calls = [record[1] for record in calls]

called_texts = [record[0] for record in texts]
receiver_texts = [record[1] for record in texts]

telemarketers = []

for number in caller_calls:
    if number not in reciever_calls and number not in called_texts and number not in receiver_texts:
        telemarketers.append(number)

telemarketers = sorted(list(set(telemarketers)))

print(f"These numbers could be telemarketers:")
for num in telemarketers:
    print(num)

