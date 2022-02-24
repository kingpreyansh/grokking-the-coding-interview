# coding: utf-8
# Problem: Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Leetcode Equivalent: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Optimal solution: O(n)

def lengthOfLongestSubstringWithoutRepeatingCharacters(s):
  windowStart, lenSubstring = 0, 0
  result = {} # create a dictionary to make sure the characters are not being repeated
  for windowEnd in range(0, len(s)): # iterate over the string
    char = s[windowEnd] # store the temporary last character
    if char in result: # if this character is in the result then simply shift the windowStart to a new location
      windowStart = max(windowStart, result[char] + 1)
    result[char] = windowEnd # if the character is not in the result then make the result[char] store the index of the character in the string
    lenSubstring = max(lenSubstring, windowEnd - windowStart + 1)
  return lenSubstring


if __name__ == "__main__":
  print(lengthOfLongestSubstringWithoutRepeatingCharacters('abcabcbb'))