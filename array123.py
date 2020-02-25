#problem
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
#
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  if len(nums) > 2:
    for i in range(len(nums)-1):
      if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
        return True
  return False
print(array123([1, 1, 2, 1, 2, 3]))