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


callers_and_times = {}
#O(n)
for call in calls:
    if call[2][3:5] == "09" and call[2][6:11].strip() == "2016":
        if call[0].strip() in callers_and_times:
            callers_and_times[call[0].strip()] += int(call[3])
        else:
            callers_and_times[call[0].strip()] = int(call[3])

        if call[1].strip() in callers_and_times:
            callers_and_times[call[1].strip()] += int(call[3])
        else:
            callers_and_times[call[1].strip()] = int(call[3])

maximum = 0
number=""
#O(n)
for key in callers_and_times.keys():
    if int(callers_and_times[key]) > maximum:
        maximum = int(callers_and_times[key])
        number = key;


print(number, " spent the longest time,", maximum, "seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

