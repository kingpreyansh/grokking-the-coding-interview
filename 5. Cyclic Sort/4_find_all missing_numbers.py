# coding: utf-8
# Problem: We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.
# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
# Leetcode Equivalent:
# Optimal solution:
#
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    # sort the array with aone pass method and once that's done
    # go through the sorted array and see which numbers are out of place
    # find the resulting array accordingly

    numsLen, i = len(nums), 0
    while i < numsLen:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    result = []
    for item in range(numsLen):
        if nums[item] != item + 1:
            result.append(item + 1)

    return result


if __name__ == "__main__":
    nums = [2, 3, 1, 8, 2, 3, 5, 1]
    print(findDisappearedNumbers(nums))
