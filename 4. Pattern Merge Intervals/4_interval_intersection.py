# coding: utf-8
# Problem: You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Leetcode Equivalent: https://leetcode.com/problems/interval-list-intersections/
# Optimal solution: O(N + M)

def intervalIntersection(interval1, interval2):
    i, j = 0, 0
    output = []
    # to make sure we iterate through both the array
    while i < len(firstList) and j < len(secondList):
        # store of values
        startFirstList = firstList[i][0]
        endFirstList = firstList[i][1]
        startSecondList = secondList[j][0]
        endSecondList = secondList[j][1]

        # if it intersects then add to result list
        if startSecondList <= endFirstList and startFirstList <= endSecondList:
            output.append([max(startFirstList, startSecondList),
                          min(endSecondList, endFirstList)])

        # depending on which list is smaller move it up that way
        if endFirstList <= endSecondList:
            i += 1
        else:
            j += 1

    # return the array
    return output


if __name__ == "__main__":
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(intervalIntersection(firstList, secondList))
