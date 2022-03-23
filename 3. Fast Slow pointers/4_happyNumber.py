# coding: utf-8
# Problem: Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
# Input: 23
# Output: true (23 is a happy number)
# Explanations: Here are the steps to find out that 23 is a happy number:
# Leetcode Equivalent: https://leetcode.com/problems/happy-number/
# Optimal solution: O(logn)

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def isHappy(n):
    def findSquare(n):
        returnNum = 0
        while n > 0:
            # get the remainder after dividing by 10  - smart way of getting the last digit
            # take 19 for example -> tempNum is 9 then
            tempNum = n % 10
            # square the last digit
            returnNum += tempNum * tempNum
            # divide by 10 and move forward
            n //= 10
        return returnNum

    # if a cycle exists and the cycle is a cycle of 1's then this means that the OG num is happy
    # if a cycle exists and the cycle is not a cycle of 1's -> unhappy num
    slowPointer, fastPointer = n, n
    while True:
        slowPointer = findSquare(slowPointer)
        fastPointer = findSquare(findSquare(fastPointer))
        if slowPointer == fastPointer:
            break
    return slowPointer == 1


if __name__ == "__main__":
    print(isHappy(19))
