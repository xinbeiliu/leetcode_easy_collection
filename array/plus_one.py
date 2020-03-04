# Given a non-empty array of digits representing a non-negative integer, plus one to
# the integer. The digits are stored such that the most significant digit is at the
# head of the list, and each element in the array contain a single digit. You may
# assume the integer does not contain any leading zero, except the number 0 itself.

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

def plus_one(digits):

    result = ''
    for num in digits:
        result += str(num)
    result = int(result)
    result += 1
    result = str(result)
    ans = []
    for num in result:
        ans.append(int(num))
    return ans


print(plus_one([1,2,9]))
