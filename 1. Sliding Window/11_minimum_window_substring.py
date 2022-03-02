# coding: utf-8
# Problem: Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Leetcode Equivalent: https://leetcode.com/problems/minimum-window-substring/
# Optimal solution:

def minWindow(s, t):

    result = {}  # this is a hashmap to keep track of the matched items
    matched, windowStart, substringStart = 0, 0, 0
    minLength = len(s) + 1  # to keep track of the minimum length of the window

    for letter in t:  # for each letter in the pattern
        if letter not in result:  # if the letter is not in the pattern
            result[letter] = 0
        result[letter] += 1  # keep a collection of items in the pattern

    for windowEnd in range(0, len(s)):
        if s[windowEnd] in result:  # if the windowEnd'th item of the string is in the pattern
            result[s[windowEnd]] -= 1  # decrement it from the hashmap
            if result[s[windowEnd]] >= 0:  # if the item still exists then increase the matched
                matched += 1

        # as long as the matched items are the same length as the pattern
        while matched == len(t):
            if minLength > windowEnd - windowStart + 1:  # update the minLength value
                minLength = windowEnd - windowStart + 1
                substringStart = windowStart

            # to slide the window forward
            if s[windowStart] in result:  # if the windowStart'th item of string is in the result
                # if the hashmap's item has 0 elements decrease the matched
                if result[s[windowStart]] == 0:
                    matched -= 1
                result[s[windowStart]] += 1
            windowStart += 1

    if minLength > len(s):  # to handle edge cases
        return ""
    return s[substringStart: substringStart + minLength]


if __name__ == "__main__":
    print(minWindow("aabdec", "abc"))
