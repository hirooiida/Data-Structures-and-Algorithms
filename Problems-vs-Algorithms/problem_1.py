def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    
    if type(number) is not int:
        print("Input value must be an integer.")
        return None

    if number < 0:
        print("Negative value is invalid.")
        return None
    elif number <= 1:
        return number

    left = 1
    right = number

    while left < right:
        mid = (left + right) // 2
        mid_sqr = mid * mid

        if mid == left:
            return left
        elif mid_sqr == number:
            return mid
        elif mid_sqr > number:
            right = mid
            continue
        elif mid_sqr < number:
            left = mid
    
    return left

print(sqrt(9))
# 3
print(sqrt(27))
# 5
print(sqrt(0))
# 0
print(sqrt(1))
# 1
print(sqrt(-1))
# Negative value is invalid.
print(sqrt("9"))
# Input value must be an integer.
