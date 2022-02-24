# coding: utf-8
# Problem: Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Leetcode Equivalent: https://leetcode.com/problems/longest-repeating-character-replacement/
# Optimal solution: O(N)

def characterReplacement(s, k):
    # the algorithm could be to find the largest window such that it contains at most k
    # non-repeating character
    windowStart, maxKLetters, longestSubstring = 0, 0, 0
    result = {}
    for windowEnd in range(0, len(s)):
        # iterate through the word
        if(s[windowEnd] not in result):
          # if the character is not in result intiate it
            result[s[windowEnd]] = 0
        # if the character is in the result increment it and the maxKLetters is going to be the maximum number of different numbers there are
        result[s[windowEnd]] += 1
        maxKLetters = max(maxKLetters, result[s[windowEnd]])

        if((windowEnd - windowStart + 1) - maxKLetters > k):
          # slide the window here if the window contains more than 2 different characters
            result[s[windowStart]] -= 1
            if(result[s[windowStart]] == 0):
                del(result[s[windowStart]])
            windowStart += 1

        longestSubstring = max(longestSubstring, windowEnd - windowStart + 1)
    return longestSubstring


if __name__ == "__main__":
    print(characterReplacement("aabccbb", 2))
