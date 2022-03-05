# coding: utf-8
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Leetcode Equivalent: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Optimal solution: O(N)

def removeDuplicates(self, nums: List[int]) -> int:
    # index of the next non-duplicate element
    next_non_duplicate = 1
    i = 1
    # while i is less than the length of the array nums
    while(i < len(nums)):
        # if the (i - 1)th element is not equal to the ith element
        if nums[next_non_duplicate - 1] != nums[i]:
            # shift the array and increase the index of the next_non_duplicate
            nums[next_non_duplicate] = nums[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


if __name__ == "__main__":
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
