# coding: utf-8
# Problem: Given a string, find the length of the longest substring in it with no more than K distinct characters.
# Example Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Leetcode Equivalent: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Optimal solution: O(n)

# TIP: whenever there is a question asking for distinct characters in a string, best to use a hashset/hashmap

def lengthOfLongestSubstringKDistinct(s, k):
  windowStart, maxLen = 0, 0 # using the sliding window approach, there's a windowStart and a maxLen (maximum length of the subarray)
  charDict = {} # to keep a track of unique characters
  for windowEnd in range(0, len(s)):  # iterate through the string
    if s[windowEnd] not in charDict: # if the item in the string is not in the dict then add it to the dict
      charDict[s[windowEnd]] = 0 
    charDict[s[windowEnd]] += 1 # else increment the item
  
    while(len(charDict) > k): # if the length of the dict is greater than k then slide the window
      charDict[s[windowStart]] -= 1
      if(charDict[s[windowStart]] == 0): # if there are no more characters then delete the key
        del(charDict[s[windowStart]])
      windowStart += 1
    maxLen = max(maxLen, windowEnd - windowStart + 1)

  return maxLen # return the maximum length through the whole iteration

if __name__ == "__main__":
  print(lengthOfLongestSubstringKDistinct("araaci", 2))