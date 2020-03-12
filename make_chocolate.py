# problem link - https://codingbat.com/prob/p190859

def make_chocolate(small, big, goal):
    max_big = goal / 5
    if max_big >= big:
        goal -= big * 5
    else:
        goal -= max_big * 5

    if goal <= small:
        return goal
    else:
        return -1

print(make_chocolate(4, 1, 7))