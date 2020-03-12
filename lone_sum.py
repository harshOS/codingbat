# problem link - https://codingbat.com/prob/p143951

def lone_sum(a, b, c):
  if a == b and b == c : return 0
  elif a == b : return c
  elif a == c : return b
  elif b == c : return a
  elif a == b and b == c : return 0
  return a+b+c

print(lone_sum(3, 3, 3))