# coding: utf-8
# Problem: Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Leetcode Equivalent:
# Optimal solution:

# for only SORTED arrays
def sortedTwoSum(nums, target):
    # have two pointers, one at the beginning one at the end
    left, right = 0, len(nums) - 1
    while left < right:  # while the left pointer is less than the right pointer keep iterating
        currentSum = nums[left] + nums[right]  # when the current
        if currentSum == target:
            return [left, right]
        if currentSum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

# for UNSORTED arrays


def twoSum(nums, target):
    hashmap = {}  # to track the numbers in the list of nums
    for i in range(len(nums)):  # for each item in the array nums
        # if target - current number exists in hashmap => pair that adds to target exists
        complement = target - nums[i]
        if complement in hashmap:  # if the complement is in the hashmap then we can return the array
            return [i, hashmap[complement]]
        # add the item to the hashmap with its value being the index number
        hashmap[nums[i]] = i


if __name__ == "__main__":
    print(twoSum([1, 2, 3, 4, 6], 6))
