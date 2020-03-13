# problem link - https://codingbat.com/prob/p160533

def close_far(a, b, c):
  if abs(a-b) <= 1 and abs(a-c) >= 2 and abs(b-c) >= 2: return True
  if abs(a-c) <= 1 and abs(a-b) >= 2 and abs(b-c) >= 2: return True
  if abs(a-c) <= 1 and abs(a-b) >= 2 and abs(b-c) >= 2: return True
  if abs(a-b) <= 1 and abs(a-c) >= 2 and abs(b-c) >= 2: return True
  return False

print(close_far(4, 1, 3)