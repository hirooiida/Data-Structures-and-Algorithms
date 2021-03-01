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

def numParser(lists, column_num):
    res_set = set()

    for list in lists:
        res_set.add(list[column_num])
    
    return res_set

out_call_num = numParser(calls, 0)
out_text_num = numParser(texts, 0)
recv_call_num = numParser(calls, 1)
recv_text_num = numParser(texts, 1)

possible_telemarketers = out_call_num - out_text_num - recv_call_num - recv_text_num

print("These numbers could be telemarketers: ")
print('\n'.join(sorted(set(possible_telemarketers))))
