# coding: utf-8
# Problem: Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# Leetcode Equivalent: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Optimal solution: O(N)

def findUnsortedSubarray(nums):
    # find the subarray which needs to be sorted
    low, high = 0, len(nums) - 1

    # find the low portion of the array where the subarray begins
    while low < len(nums) - 1 and nums[low + 1] >= nums[low]:
        low += 1

    if low == len(nums) - 1:
        return 0

    # find the high portion of the array where the subarray ends
    while nums[high] >= nums[high - 1] and high > 0:
        high -= 1

    maxOfSubarray = -9999
    minOfSubarray = 9999

    for i in range(low, high + 1):
        maxOfSubarray = max(maxOfSubarray, nums[i])
        minOfSubarray = min(minOfSubarray, nums[i])

    while low > 0 and nums[low - 1] > minOfSubarray:
        low -= 1

    while high < len(nums) - 1 and nums[high + 1] < maxOfSubarray:
        high += 1

    return high - low + 1


if __name__ == "__main__":
    print(findUnsortedSubarray([1, 3, 2, 4, 5]))
