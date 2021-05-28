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

# Get all the out going callers
possible_telemarketers = set()

for call in calls:
    possible_telemarketers.add(call[0].strip())
# print(len(possible_telemarketers))
# Start disqualifying numbers
for call in calls:
    if call[1].strip() in possible_telemarketers:
        possible_telemarketers.remove(call[1].strip())

for text in texts:
    if text[0] in possible_telemarketers:
        possible_telemarketers.remove(text[0].strip())
    if text[1] in possible_telemarketers:
        possible_telemarketers.remove(text[1].strip())

# print(len(possible_telemarketers))
print("These numbers could be telemarketers: ")
for number in sorted(possible_telemarketers):
    print(number)

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

