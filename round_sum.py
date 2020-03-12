# problem link - https://codingbat.com/prob/p179960

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    n = num % 10
    if n < 5:
        num -= n
    else:
        num += (10 - n)
    return num
print(round_sum(6, 4, 4))