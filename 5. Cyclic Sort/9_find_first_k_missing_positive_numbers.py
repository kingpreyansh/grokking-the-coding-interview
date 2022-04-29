# coding: utf-8
# Problem: Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.
# Input: [3, -1, 4, 5, 5], k=3
# Output: [1, 2, 6]
# Explanation: The smallest missing positive numbers are 1, 2 and 6.
# Leetcode Equivalent: N/A
# Optimal solution:

def find_first_k_missing_positive_numbers(nums, k):
    # sort the array with a cyclic sort
    # find the missing numbers within the range of length of nums
    # find the missing numbers outside the range of the length of nums
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missingNumbers = []
    for i in range(n):
        if len(missingNumbers) < k and nums[i] != i + 1:
            missingNumbers.append(i + 1)
    i = 1

    while len(missingNumbers) < k:
        potentialNum = i + n
        if potentialNum not in missingNumbers and potentialNum not in nums:
            missingNumbers.append(potentialNum)
        i += 1
    return missingNumbers


if __name__ == "__main__":
    nums = [2, 3, 4]
    k = 3
    print(find_first_k_missing_positive_numbers(nums, k))
