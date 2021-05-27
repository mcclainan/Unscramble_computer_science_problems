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

text = texts[0]
print("First record of texts,", text[0], "texts", text[1], "at time", text[2])
call = calls[len(calls)-1]
print("Last record of calls,", call[0], "calls", call[1], "at time", call[2], ", lasting", call[3], "seconds")

# Time complexity is O(1) since the same amount of operations will occur regardless to the size of the data
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
