# coding: utf-8
# Problem: Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# Leetcode Equivalent: https://leetcode.com/problems/fruit-into-baskets/
# Optimal solution: O(n)

def totalFruit(fruits):
  windowStart, totalLen = 0, 0
  result = {}
  for windowEnd in range(0, len(fruits)):
    if(fruits[windowEnd] not in result):
      result[fruits[windowEnd]] = 1
    else:
      result[fruits[windowEnd]] += 1
    
    while len(result) > 2:
      result[fruits[windowStart]] -= 1
      if(result[fruits[windowStart]] == 0):
        del(result[fruits[windowStart]])
      windowStart+=1
    totalLen = max(totalLen, windowEnd - windowStart + 1)

  return totalLen

if __name__ == "__main__":
  print(totalFruit(['A', 'B', 'C', 'A', 'C']))




