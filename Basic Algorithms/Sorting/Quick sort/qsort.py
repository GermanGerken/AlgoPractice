def qsort(array):

    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return qsort(less) + [pivot] + qsort(greater)


print(qsort([24,6,67,45,632,363,6322,9876,3,4,56,7,8,2,1,84,50]))