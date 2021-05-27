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

# iterate over both lists and find the unique phone numbers
phone_numbers = set()
for record in texts + calls:
    phone_numbers.add(record[0])
    phone_numbers.add(record[1])

# Output the count of the unique numbers
print("There are ", len(phone_numbers), " different telephone numbers in the records.")

# Time complexity is O(n) as the number of operations will increase proportionately to the data size
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
