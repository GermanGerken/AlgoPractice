from utils.tools import time_execution


# This function performs a linear search through the list to find the specified item.
@time_execution
def stupid_search(list_, item):
    for i, e in enumerate(list_):
        if e == item:
            return i
    return None


# This function performs a binary search on a sorted list to find the specified item.
@time_execution
def binary_search(list_, item):
    low = 0
    high = len(list_) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list_[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


# Create a list of integers from 1 to 1,000,000
my_list = list(range(1, 1000001))

# Test the binary search function
print(binary_search(my_list, 999))  # --> 1
print(binary_search(my_list, -1))  # --> None

# Test the linear search function
print(stupid_search(my_list, 999))  # --> 1
print(stupid_search(my_list, -1))  # --> None
