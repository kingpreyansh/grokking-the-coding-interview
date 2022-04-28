# coding: utf-8
# Problem: Given an unsorted array containing numbers, find the smallest missing positive number in it.
# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'
# Leetcode Equivalent: https://leetcode.com/problems/first-missing-positive/
# Optimal solution:

def firstMissingPositive(nums):
    # sort the numbers array (ignore the negative numbers)
    # once sorted, see which index is out of place and return that
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    nums = [1, 2, 0]
    print(firstMissingPositive(nums))
