# coding: utf-8
# Problem: Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Explanation:
# Leetcode Equivalent: https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Optimal solution:

def findDuplicates(nums):
    # works but it's really slow
    # 1. sort the array with O(n) time
    # 2. build an array everytime we encounter a duplicate -> duplicate = not the right number and the right spot is filled

    result = []
    i, n = 0, len(nums)
    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                if nums[i] not in result:
                    result.append(nums[i])
                i += 1
        else:
            i += 1
    return result


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDuplicates(nums))
