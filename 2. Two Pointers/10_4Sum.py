# coding: utf-8
# Problem: find a quadruplet that adds to the target
# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.
# Leetcode Equivalent:
# Optimal solution: O(N^3)

def fourSum(nums, target):
    # sort the array to be able to use the two pointers approach
    nums.sort()
    res, quad = [], []

    def kSum(k, start, target):
        # normal case when k is not 2
        if k != 2:
            # to have enough space for a subarray of size k
            for i in range(start, len(nums) - k + 1):
                # if the nums[i] is different than nums[i-1] then skip this iteration because we don't want duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # append nums[i] to the list of arrays
                quad.append(nums[i])
                # call kSum on (k - 1) subarrays with i + 1 as the start index and target - nums[i] as the new target
                kSum(k - 1, i + 1, target - nums[i])
                # pop the item from the quad array
                quad.pop()
            return

        # base case, call two sum
        l, r = start, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                res.append(quad + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l - 1] == nums[l]:
                    l += 1

    kSum(4, 0, target)
    return res


if __name__ == "__main__":
    print(fourSum([1, 0, -1, 0, -2, 2], 0))
