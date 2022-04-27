# coding: utf-8
# Problem:
# Input: [1, 4, 4, 3, 2]
# Output: 4
# Explanation:
# Leetcode Equivalent: https://leetcode.com/problems/find-the-duplicate-number/submissions/
# Optimal solution:

def find_duplicate(nums):
    n, i = len(nums), 0
    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                # swap when its not in the right spot
                nums[i], nums[j] = nums[j], nums[i]
            else:
                # at this point nums[i] != i + 1 and it's not at the right spot which means its a duplicate
                return nums[i]
        else:
            i += 1

    return -1


if __name__ == "__main__":
    nums = [1, 4, 4, 3, 2]
    print(find_duplicate(nums))
