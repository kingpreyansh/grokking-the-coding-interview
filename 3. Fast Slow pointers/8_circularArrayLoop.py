# coding: utf-8
# Problem: We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:
# If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
# If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
# Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.
# Input: [1, 2, -1, 2, 2]
# Output: true
# Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
# Leetcode Equivalent: https://leetcode.com/problems/circular-array-loop/
# Optimal solution: O(N^2) time complexity and O(1) space complexity.

def find_next_index(givenDirection, nums, index):
    currDirection = nums[index] >= 0
    if currDirection != givenDirection:
        return -1

    nextIndex = (index + nums[index]) % len(nums)
    if nextIndex == index:
        nextIndex = -1

    return nextIndex


for i in range(len(nums)):
    currDirection = nums[i] >= 0
    slow, fast = i, i
    while True:
        slow = find_next_index(currDirection, nums, slow)
        fast = find_next_index(currDirection, nums, fast)
        if fast != -1:
            fast = find_next_index(currDirection, nums, fast)

        if slow == -1 or fast == -1 or slow == fast:
            break

    if slow != -1 and slow == fast:
        return True

return False

if __name__ == "__main__":
    nums = [2, -1, 1, 2, 2]
    print(circularArrayLoop(nums))
