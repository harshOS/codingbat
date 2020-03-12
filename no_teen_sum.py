# problem link - https://codingbat.com/prob/p100347

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if n == 15 or n == 16:
        return n
    elif n >= 13 and n <= 19:
        return 0
    else:
        return n
print(no_teen_sum(2, 1, 14))