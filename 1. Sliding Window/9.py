# coding: utf-8
# Problem: Given a string and a pattern, find out if the string contains any permutation of the pattern.
# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Leetcode Equivalent: https://leetcode.com/problems/permutation-in-string/
# Optimal solution:
def checkInclusion(s1, s2):
    s1Dict = {}
    s2Dict = {}
    windowStart = 0
    # considering that s1 needs to be smaller or equal to s2 to be true
    if(len(s1) > len(s2)):
        return False

    for i in range(0, len(s1)):
        if s1[i] not in s1Dict:
            s1Dict[s1[i]] = 0
        s1Dict[s1[i]] += 1

    for windowEnd in range(0, len(s2)):
        if s2[windowEnd] not in s2Dict:
            s2Dict[s2[windowEnd]] = 0
        s2Dict[s2[windowEnd]] += 1

        if(windowEnd - windowStart + 1 > len(s1)):
            s2Dict[s2[windowStart]] -= 1
            if(s2Dict[s2[windowStart]] == 0):
                del(s2Dict[s2[windowStart]])
            windowStart += 1

        if(s1Dict == s2Dict):
            return True
    return False


if __name__ == "__main__":
    print(checkInclusion("ab", "eidbaooo"))
