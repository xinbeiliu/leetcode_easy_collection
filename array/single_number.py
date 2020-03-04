# Given a non-empty array of integers, every element appears twice except for one.
# Find that single one.Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?
#
# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

def single_num(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] not in result:
            result.append(nums[i])
        else:
            result.remove(nums[i])
    return result.pop()

print(single_num([2,2,1]))
print(single_num(([4,1,2,1,2])))