# coding: utf-8
# Problem: Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
# Example input: [2, 1, 5, 1, 3, 2], k=3
# Output: [5, 1, 3] 
# Leetcode Equivalent: https://leetcode.com/problems/maximum-subarray/ (Close enough)
# Optimal solution: 
# Brute Force solution: 

def max_sliding_window(array, k):
  windowSum, windowStart = 0.0, 0 #need a total sum and a windowStart
  result = []
  for windowEnd in range(len(array)):
    windowSum += array[windowEnd]
    if(windowEnd >= k - 1):
      result.append(windowSum)
      windowSum-=array[windowStart]
      windowStart+=1
  return max(result)

if __name__ == "__main__":
  print(max_sliding_window([2, 1, 5, 1, 3, 2], 3))


