# coding: utf-8
# Problem: Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.
# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# Leetcode Equivalent:https://leetcode.com/problems/backspace-string-compare/
# Optimal solution: O(M + N)

def backspaceCompare(S, T):
    def buildString(s):
        q = []
        i = 0
        while i < len(s):
            if s[i] != "#":
                q.append(s[i])
            elif len(q) > 0:
                q.pop()
            i += 1
        return q

    return buildString(S) == buildString(T)


if __name__ == "__main__":
    print(backspaceCompare("xy#z", "xzz#"))
