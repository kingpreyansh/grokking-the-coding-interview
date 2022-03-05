# coding: utf-8
# Problem: Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Leetcode Equivalent: https://leetcode.com/problems/squares-of-a-sorted-array/
# Optimal solution: O(N)

def sortedSquares(nums):
    # Create two pointers -- one for the leftMost square and one for the rightMost
    # Both these pointers will meet in the middle in the very last iteration causing O(N) time
    leftPointer = 0
    rightPointer = len(nums) - 1

    # our return array
    result = [0 for x in range(len(nums))]

    # This is to keep track of the right most available index on the result array
    highestSquare = len(nums) - 1

    # While the left pointer is less than equal to the right pointer keep iterating
    while leftPointer <= rightPointer:
        # the left and right values squared
        leftSquare = nums[leftPointer] * nums[leftPointer]
        rightSquare = nums[rightPointer] * nums[rightPointer]

        # if the leftSquare < rightSquare then add the rightSquare onto the right-most portion of the array
        # esle add the leftSquare onto the right-most portion of the array
        if leftSquare < rightSquare:
            result[highestSquare] = rightSquare
            rightPointer -= 1
        else:
            result[highestSquare] = leftSquare
            leftPointer += 1
        highestSquare -= 1
    # return the result array
    return result


if __name__ == "__main__":
    print(sortedSquares([-4, -1, 0, 3, 10]))
