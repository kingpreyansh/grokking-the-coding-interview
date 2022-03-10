# coding: utf-8
# Problem: Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Leetcode Equivalent: https://leetcode.com/problems/3sum-closest/
# Optimal solution: O(N^2)


def threeSumClosest(nums, target):
    # to calculate the closest will have to use the formula closestSum = min(closestSum, a + b + c - target)
    diff = 9999
    # sort the array to use two pointers approach
    nums.sort()
    for i in range(len(nums)):
        # initialize the low and high pointers
        lo, hi = i + 1, len(nums) - 1
        # while the low pointer < high pointer keep iterating
        while (lo < hi):
            # compute the currentSum
            sum = nums[i] + nums[lo] + nums[hi]
            # if the current distance is less than min distance then update min distance
            if abs(target - sum) < abs(diff):
                diff = target - sum
                # if the sum < target move pointer accordingly
            if sum < target:
                lo += 1
                # if the sum < target move pointer accordingly
            else:
                # in both cases where sum > target and sum == target both cases decrease the high pointer
                hi -= 1
        # no more iterations if the perfect triplet has been found
        if diff == 0:
            break
    return target - diff


if __name__ == "__main__":
    print(threeSumClosest([-1, 2, 1, -4], 1))
