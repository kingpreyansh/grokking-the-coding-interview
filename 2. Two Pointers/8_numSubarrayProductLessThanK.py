# coding: utf-8
# Problem: Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Leetcode Equivalent: https://leetcode.com/problems/subarray-product-less-than-k/
# Optimal solution: O(N)

def numSubarrayProductLessThanK(nums, k):
  # a sliding window shoudl be used because the problem involves contiguous subarrays
    windowStart, product, totalNum = 0, 1, 0
    # if the total product <= 1 then automatically return 0
    if k <= 1:
        return 0
    # iterate through the list of integers
    for windowEnd in range(0, len(nums)):
        # to keep a track of the product of the items in the window
        product *= nums[windowEnd]
        # the second the window contains items w which the product is < k
        while product >= k:
          # decrease the size of the window
            product /= nums[windowStart]
            windowStart += 1
        # the number of combinations of products is the length of the window
        totalNum += windowEnd - windowStart + 1
    return totalNum


if __name__ == "__main__":
    print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
