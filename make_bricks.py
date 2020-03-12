#problem link - https://codingbat.com/prob/p118406

def make_bricks(small, big, goal):
#return ((goal / 5) <= big and (goal % 5) <= small)
  big_max = goal / 5
  if big_max <= big:
    goal -= big_max*5
  else: goal -= big*5
  if goal <= small:
    return True
  else:
    return False

print(make_bricks(3, 2, 10))