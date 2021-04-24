def sort_a_little_bit(items, begin_index, end_index):    
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1
    
    return pivot_index


def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    

def quicksort(items):
    sort_all(items, 0, len(items) - 1)


def rearrange_digits(input_list):
    if input_list == []:
        return []
    
    if type(input_list) is not list:
        return None

    quicksort(input_list)

    left = []
    right = []
    
    for i in range(len(input_list))[::-1]:
        if i % 2 == 0:
            left.append(str(input_list[i]))
        else:
            right.append(str(input_list[i]))

    return [int(''.join(left)), int(''.join(right))]


print(rearrange_digits([1, 2, 3, 4, 5]))
# [531, 42]
print(rearrange_digits([4, 6, 2, 5, 9, 8]))
# [852, 964]
print(rearrange_digits([4, 6, 2, 5, 9, 8, 1, 3, 7]))
# [97531, 8642]
print(rearrange_digits([1, 2]))
# [1, 2]
print(rearrange_digits([]))
# []
print(rearrange_digits(5))
# None