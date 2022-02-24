# coding: utf-8
# Problem: Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Leetcode Equivalent: https://leetcode.com/problems/max-consecutive-ones-iii/
# Optimal solution: O(N)

def longestOnes(nums, k):
    windowStart, maxOneCount, largestReturn = 0, 0, 0
    for windowEnd in range(0, len(nums)):
        if nums[windowEnd] == 1:
            maxOneCount += 1

        if((windowEnd - windowStart + 1) - maxOneCount > k):
            if(nums[windowStart] == 1):
                maxOneCount -= 1
            windowStart += 1
        largestReturn = max(largestReturn, windowEnd - windowStart + 1)
    return largestReturn


if __name__ == "__main__":
    print(longestOnes([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
