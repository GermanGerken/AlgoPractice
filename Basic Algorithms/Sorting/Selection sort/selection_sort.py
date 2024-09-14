from utils.tools import time_execution

@time_execution
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


print(findSmallest([5, 3, 6, 2, 10]))

@time_execution
def ssort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(ssort([24,6,67,45,632,363,6322,9876,3,4,56,7,8,2,1,84,50]))
