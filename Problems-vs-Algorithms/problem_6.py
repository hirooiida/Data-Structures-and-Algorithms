def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_val = None
    max_val = None

    for index, value in enumerate(ints):
        if index == 0:
            min_val = value
            max_val = value
        elif value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    return (min_val, max_val)

ints = [8,2,5,7,4,5,9,1,3]
print(get_min_max(ints))
# (1,9)

ints = [1]
print(get_min_max(ints))
# (1,1)

ints = []
print(get_min_max(ints))
# (None,None)
