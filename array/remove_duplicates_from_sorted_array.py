# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.

# example 1
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.

#example 2
# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with the first five elements of
# nums being modified to 0, 1, 2, 3, and 4 respectively.
#
# It doesn't matter what values are set beyond the returned length.

def remove_dup(nums):
    # two pointers: i is the slow runner and j is the fast runner
    # when encounter an element, bypass the duplicates and move
    # on to the next element
    # since nums are sorted, reassign the element when a non duplicate
    # element is encountered

    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

print(remove_dup([[0,0,1,1,1,2,2,3,3,4]]))
