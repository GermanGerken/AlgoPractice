from utils.tools import time_execution


def sum_(array_):
    if len(array_) == 0:
        return 0
    return array_.pop(0) + sum_(array_)

def count_(array_):
    if len(array_) == 0:
        return 0
    return 1 + count_(array_[1:])

def max_(array_):
    if len(array_) == 2:
        return array_[0] if array_[0] > array_[1] else array_[1]
    submax = max(array_[1:])
    return array_[0] if array_[0] > submax else submax


li = [1, 23, 4, 5]

print(sum_(li))

li = [1, 23, 4, 5]
print(count_(li))

li = [1, 23, 4, 5]
print(max_(li))