# coding: utf-8
# Problem: Given an array of positive numbers and a positive number ‘s’, 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
# Return 0, if no such subarray exists.
# Example input: [2, 1, 5, 2, 3, 2], S=7 
# Leetcode Equivalent: https://leetcode.com/problems/minimum-size-subarray-sum/
# Optimal solution: 

def minSubArrayLen(array, s):
  # We need variables for windowStart, windowEnd, windowSum and minWindow
  # Each of these variables serve its duty and their tasks can be inferred from their variable name
  windowSum, windowStart = 0.0, 0
  minWindow = 999999
  for windowEnd in range(len(array)):
    windowSum = sum(array[windowStart: windowEnd])
    while(sum(array[windowStart: windowEnd]) >= s):
      minWindow = min(len(array[windowStart: windowEnd]), minWindow)
      windowStart+=1

  return minWindow

if __name__ == "__main__":
  print(minSubArrayLen([2, 1, 5, 2, 3, 2], 7))