# coding: utf-8
# Problem: Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Example input: Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Brute Force solution: O(n*k) 
# Optimal solution: O(n)

def brute_force_average_of_subarray(array, K):
  # 1) going to first make sure than K is less than or equal to size of array
  # 2) start off with the first K elements in the array
  # 3) track the first number and then go on to the next K elements of the array
  result = []
  for index in range(0, len(array) - K + 1):
    _sum = 0.0
    for index2 in range(index, K + index):
      _sum+=array[index2]
    result.append(_sum/K)
  return result

def optimal_sliding_window(array, k):
  # go through the first k elements of the array adding
  windowSum, windowStart = 0.0, 0 # windowSum is a floating value and will be used to keep a track of the sum and windowStart is to keep track of the index when it slides over
  result = [] # this result array is going to contain the averages of the window
  for windowEnd in range(len(array)): # windowEnd is the index which will shift over once the window hits K
    windowSum += array[windowEnd]
    if(windowEnd >= k - 1):
      result.append(windowSum/k)
      windowSum -= array[windowStart]
      windowStart+=1
  return result


if __name__ == "__main__":
  print(brute_force_average_of_subarray([1,2,3,4], 2))
  print(optimal_sliding_window([1,2,3,4], 2))



