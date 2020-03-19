#problem link - https://codingbat.com/prob/p167025

def sum13(nums):
    sum1 = 0
    for i in range(len(nums)):
        if nums[i] != 13:
            sum1 += nums[i]
        elif i < (len(nums)-1) and nums[i+1] != 13:
            sum1 -= nums[i+1]
    return sum1
