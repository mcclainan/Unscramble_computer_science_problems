"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def get_length(phone_call):
    if phone_call[2][3:5] != "09" or phone_call[2][6:11].strip() != "2016":
        return 0
    return int(phone_call[3].strip())


longest_time = 0
phone_number = ""
for call in calls:
    if get_length(call) > longest_time:
        longest_time = int(call[3])
        phone_number = call[0]

print(phone_number, " spent the longest time,", longest_time, "seconds, on the phone during September 2016.")


# Time complexity is O(n) as the number of operations will increase proportionately to the data size
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

