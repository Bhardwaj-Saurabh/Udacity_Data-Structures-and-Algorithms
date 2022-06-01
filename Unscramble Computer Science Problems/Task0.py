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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# First Text records
ft_ic = texts[0][0]
ft_oc = texts[0][1]
ft_time = texts[0][-1]

# Last call records
lc_ic = calls[0][0]
lc_oc = calls[0][1]
lc_time = calls[0][2]
lc_duration = calls[0][-1]

print(f"First record of texts, {ft_ic} texts {ft_oc} at time {ft_time}")
print(f"Last record of calls, {lc_ic} calls {lc_oc} at time {lc_time}, lasting {lc_duration} seconds")
