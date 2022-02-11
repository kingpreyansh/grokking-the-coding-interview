# coding: utf-8
# Problem: Given an array of positive numbers and a positive number ‘s’, 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
# Return 0, if no such subarray exists.
# Example input: [2, 1, 5, 2, 3, 2], S=7 
# Leetcode Equivalent: https://leetcode.com/problems/minimum-size-subarray-sum/
# Optimal solution: O(n) The outer for loop runs for all elements and the inner while loop processes each element only once, therefore the time complexity of the algorithm will be O(N+N)O(N+N) which is asymptotically equivalent to O(N)O(N).

def minSubArrayLen(self, array, s):
  windowSum, windowStart = 0.0, 0 
  minWindow = 9999999

  for windowEnd in range(0, len(array)): # to increase the window size while we move forward
    windowSum += array[windowEnd] # to increase the sum of the window
    while(windowSum >= s): # keep decreasing the window and try to find the most minimal size that satisfies our condition
      minWindow = min(windowEnd - windowStart + 1, minWindow) 
      windowSum -= array[windowStart] # when the window slides the first element gets cut from the sum
      windowStart += 1 # shifting the window over
  
  if minWindow == 9999999:
    return 0
  return minWindow

if __name__ == "__main__":
  print(minSubArrayLen([2,3,1,2,4,3], 7))
