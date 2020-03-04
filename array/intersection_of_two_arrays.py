# Given two arrays, write a function to compute their intersection.

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# followup
# What if the given array is already sorted?
# How would you optimize your algorithm?
# [4,5,9] [4,4,8,9,9]

def inter_two_arr(nums1, nums2):
    result = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            result.append(nums1[i])
    return result

# print(inter_two_arr([1,2,2,1], [2,2]))
# print(inter_two_arr([4,9,5], [9,4,9,8,4]))

# using sorting
# [4,5,9] [4,4,8,9,9]
def inter_two_arr2(nums1, nums2):
    result = []
    i, j= 0, 0
    nums1.sort()
    nums2.sort()
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1
    return result

print(inter_two_arr2([1,2,2,1],[2,2]))
print(inter_two_arr2([4,9,5], [9,4,9,8,4]))
