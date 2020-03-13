# problem link - https://codingbat.com/prob/p107863


def lucky_sum(a, b, c):
  if a == 13 : return 0
  elif b == 13: return a
  elif c == 13 : return  a+b
  return a+b+c

print(lucky_sum(1, 2, 13))