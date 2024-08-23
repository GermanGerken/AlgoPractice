from utils.tools import time_execution


def findSmallest(arr):
    # для хранения наименьшего значения
    smallest = arr[0]
    # для хранения индекса наименьшего значения
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


print(findSmallest([5, 3, 6, 2, 10]))
