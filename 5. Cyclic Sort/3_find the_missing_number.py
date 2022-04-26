# coding: utf-8
# Problem: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Leetcode Equivalent:
# Optimal solution:
#
def find_missing_number(nums):
    # basically sort the array using cyclic sort method
    # iterate through the array
    # if a number is not in the array return that number
    length = len(nums)
    for i in range(length):
        j = nums[i]
        if j < length and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(length):
        if nums[i] != i:
            return i

    return length


if __name__ == "__main__":
    nums = [3, 0, 1]
    print(find_missing_number(nums))
