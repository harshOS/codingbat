# Warmup-1 > diff21
# problem 2
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
  if n > 21:
    return 2*(n-21)
  else:
    return 21 - n

print(diff21(18))