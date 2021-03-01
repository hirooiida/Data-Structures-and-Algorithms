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

phone_nums = set()
phone_dict = {}

for i in range(len(calls)):
    tx_num   = calls[i][0]
    rx_num   = calls[i][1]
    duration = int(calls[i][3])

    if tx_num not in phone_dict:
        phone_dict[tx_num] = duration
    elif tx_num in phone_dict:
        phone_dict[tx_num] += duration

    if rx_num not in phone_dict:
        phone_dict[rx_num] = duration
    elif rx_num in phone_dict:
        phone_dict[rx_num] += duration

max_key = max(phone_dict, key=phone_dict.get)
max_val = max(phone_dict.values())

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key, max_val))
