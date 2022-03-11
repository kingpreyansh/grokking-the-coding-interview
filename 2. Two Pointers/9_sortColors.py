# coding: utf-8
# Problem: Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# Input: [1, 0, 2, 1, 0]
# Output: [0 0 1 1 2]
# Explanation: Array is sorted
# Leetcode Equivalent: https://leetcode.com/problems/sort-colors/
# Optimal solution: O(N) - one pass

def sortColors(nums):
  # three pointers: i to iterate the array, lo to keep track of where the '0' will go and hi to keep track where the '2' will go
    lo, hi, i = 0, len(nums) - 1, 0
    # iterate till the ith iteration meets the last index
    while i <= hi:
      # if the current iteration is a 0 then swap the 0 to the 'lo' spot with the ith spot
        if nums[i] == 0:
            nums[i], nums[lo] = nums[lo], nums[i]
            i += 1
            lo += 1
        elif nums[i] == 1:
            # if the iteration is a 1 then do nothing
            i += 1
        else:
            nums[hi], nums[i] = nums[i], nums[hi]
            # we decrease the index of the hi pointer to ensure we have the next spot where the '2' can go to
            # notice we do not increment i because if the swap with the '2' is a '1' then we would be in trouble
            hi -= 1
    return nums


if __name__ == "__main__":
    print(sortColors([2, 0, 2, 1, 1, 0]))
