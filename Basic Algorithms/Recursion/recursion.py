from utils.tools import time_execution


@time_execution
def look_for_key(pile):
    while pile:
        box = pile.pop()
        for i in box:
            if type(i) == list:
                pile.append(i)
            else:
                print('Find a key')
                return 1


# pile = [[[], [], [], []], [[], [[[], []], []], []], [[], 1], [[], []], [], []]
# look_for_key(pile)


@time_execution
def look_for_key_r(bоx):
    for item in bоx:
        if type(item) == list:
            look_for_key_r(item)
        elif item == 1:
            print("found the key!")
            return 1


# pile = [[[], [], [], []], [[], [[[], []], []], []], [[], 1], [[], []], [], []]
# look_for_key_r(pile)

@time_execution
def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fact(x - 1)


print(fact(0))
