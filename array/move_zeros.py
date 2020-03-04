# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# using extra space
def move_zeros(nums):
    ans_1 = []
    ans_2 = []
    for i in range(len(nums)):
        if nums[i] != 0:
            ans_1.append(nums[i])
        elif nums[i] == 0:
            ans_2.append(nums[i])
    return ans_1 + ans_2

print(move_zeros([0,1,0,3,12]))

# in place using two pointers
def move_zeros2(nums):
    i, j = 0, 1
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
    return nums

print(move_zeros2([0,1,0,3,12]))

