#problem link - https://codingbat.com/prob/p189616

def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0 : count += 1
  return count

print(count_evens([1, 3, 5]))