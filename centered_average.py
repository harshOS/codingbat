#problem link  - https://codingbat.com/prob/p126968

def centered_average(nums):
  nums.remove(max(nums))
  nums.remove(min(nums))
  return sum(nums)/len(nums)