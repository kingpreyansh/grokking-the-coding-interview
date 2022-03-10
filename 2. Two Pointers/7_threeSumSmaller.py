# coding: utf-8
# Problem: Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
# Input: [-1, 0, 2, 3], target=3
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# Leetcode Equivalent: https://leetcode.com/problems/3sum-smaller/
# Optimal solution:
def threeSumSmaller(nums, target):
    # to keep a track of items that are less than the target
    sumLessThan = 0
    # sort the array to be able to use two pointers approach
    nums.sort()
    # iterate through the array of nums
    for i in range(0, len(nums)):
        # initiate the two pointers
        p1, p2 = i + 1, len(nums) - 1
        # while the first pointer < second pointer
        while p1 < p2:
            # if the sum of the triplet < target then all the sums with pointer < p2 must also be < target since the array is sorted and hence all the numbers in indices <p2 must be less than the number in p2 and still sum to less than the target
            if nums[i] + nums[p1] + nums[p2] < target:
                # add the combinations less than p2 which would still be valid and increment p1
                sumLessThan += p2 - p1
                p1 += 1
            else:
                # decrease p2 if sum > target or sum == target
                p2 -= 1
    return sumLessThan


if __name__ == "__main__":
    print(threeSumSmaller([-2, 0, 1, 3], 2))
