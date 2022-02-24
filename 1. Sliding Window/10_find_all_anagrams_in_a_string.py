# coding: utf-8
# Problem: Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Leetcode Equivalent:
# Optimal solution:
def findAnagrams(s, p):
    sDict, pDict = {}, {}
    returnArray = []
    windowStart = 0

    # Formulate the pDict
    for i in range(0, len(p)):
        if p[i] not in pDict:
            pDict[p[i]] = 0
        pDict[p[i]] += 1

    for windowEnd in range(0, len(s)):
        if s[windowEnd] not in sDict:
            sDict[s[windowEnd]] = 0
        sDict[s[windowEnd]] += 1
        if(windowEnd - windowStart + 1 > len(p)):
            sDict[s[windowStart]] -= 1
            if sDict[s[windowStart]] == 0:
                del(sDict[s[windowStart]])
            windowStart += 1
        if(pDict == sDict):
            returnArray.append(windowEnd + 1 - len(p))

    return returnArray


if __name__ == "__main__":
    print(findAnagrams("cbaebabacd", "abc"))
