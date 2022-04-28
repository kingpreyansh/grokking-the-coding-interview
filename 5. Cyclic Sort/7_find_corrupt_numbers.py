# coding: utf-8
# Problem: We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.
# Input: [3, 1, 2, 5, 2]
# Output: [2, 4]
# Explanation: '2' is duplicated and '4' is missing.
# Leetcode Equivalent:
# Optimal solution:

def find_corrupt_numbers(nums):
    # sort the array using cyclical sort
    # after it's sorted iterate through the array and try to find the duplicate
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            # at this point the nums array is sorted
            return [nums[i], i + 1]


if __name__ == "__main__":
    nums = [3, 1, 2, 3, 6, 4]  # -> [1, 2, 3, 4, 3, 6]
    print(find_corrupt_numbers(nums))
