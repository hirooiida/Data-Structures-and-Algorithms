def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if type(input_list) is not list:
        return -1
    
    if input_list == []:
        return -1
    
    left_index = 0
    right_index = len(input_list) - 1

    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        
        left_value = input_list[left_index]
        mid_value = input_list[mid_index]
        right_value = input_list[right_index]

        '''
        print("\n")
        print("target: {}".format(number))
        print("left index: {}".format(left_index))
        print("mid index: {}".format(mid_index))
        print("right index: {}".format(right_index))
        print(input_list[left_index:right_index+1])
        '''

        if mid_index == left_index and mid_value != number:
            return -1

        if mid_value == number:
            return mid_index
        elif right_value == number:
            return right_index
        elif left_value == number:
            return left_index
        
        '''
        case1: 1,2,3,4,5,6,7  left < mid < right
        case2: 5,6,7,1,2,3,4  mid < right < left
        case3: 3,4,5,6,7,1,2  right < left < mid
        '''
        if left_value < mid_value < right_value:
            if number > mid_value:
                left_index = mid_index
                continue
            else:
                right_index = mid_index
                continue
        elif mid_value < right_value < left_value:
            if mid_value < number <= right_value:
                left_index = mid_index
                continue
            else:
                right_index = mid_index
                continue
        elif right_value < left_value < mid_value:
            if number > mid_value or number <= right_value:
                left_index = mid_index
                continue
            else:
                right_index = mid_index
        
    if input_list[right_index] == number:
        return right_index

            
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 2))
# 6
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
# 0
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 4))
# 8
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 0))
# -1
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 11))
# -1
print(rotated_array_search([], 2))
# -1
print(rotated_array_search("MyList", 2))
# -1
