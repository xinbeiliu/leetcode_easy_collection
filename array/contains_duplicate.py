# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
# example 1
# Input: [1,2,3,1]
# Output: true

# works for smaller size of array
def check_dup(nums):
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            return True
    return False

# time complexity O^2

print(check_dup([1,1,1,3,3,4,3,2,4,2]))

# works for larger size of array
def check_dup2(nums):
    result = {}
    for i in range(len(nums)):
        if nums[i] in result:
            return True
        result[nums[i]] = 1
    return False

print(check_dup2([1,1,1,3,3,4,3,2,4,2]))