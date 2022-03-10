# coding: utf-8
# Problem: Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Leetcode Equivalent: https://leetcode.com/problems/3sum/solution/
# Optimal solution: O(N^2)

def threeSum(nums):
    # Algorithm:
    # 1) sort the array: [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]
    # 2) pick the ith item in the array nums[i] and see if a pair exists in [-1, -1, 0, 1, 2] that adds to -nums[i]
    # 3) if it does add to the array (using two pointers) else go to the next iteration
    # 4) add to the result array

    # sort the array
    nums.sort()
    # array that I will add the triplets to
    result = []
    # iterate every item in the array
    for i in range(0, len(nums)):
        # make sure duplicates are avoided
        if i == 0 or nums[i - 1] != nums[i]:
            # create the two pointers
            p1 = i + 1
            p2 = len(nums) - 1
            # as long as the first pointer < last pointer keep iterating
            while p1 < p2:
                # add the sum
                sum = nums[p1] + nums[p2] + nums[i]
                # if sum < 0 then increase the left pointer
                if sum < 0:
                    p1 += 1
                # if sum > 0 then increase the right pointer
                elif sum > 0:
                    p2 -= 1
                # if sum == 0 then move to the next pair and make sure the duplicates are being counted
                else:
                    result.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1 - 1] == nums[p1]:
                        p1 += 1
    # return the result
    return result


if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))
