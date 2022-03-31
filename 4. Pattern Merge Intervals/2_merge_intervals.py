# coding: utf-8
# Problem: This pattern describes an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if they overlap.
# Example Problem: Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
# one [1,5].
# Leetcode Equivalent: https://leetcode.com/problems/merge-intervals/
# Optimal solution: O(N*logN)

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    if len(intervals) < 2:
        return intervals

    output = [intervals[0]]
    for start, end in intervals[1:]:
        lastEnd = output[-1][1]
        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])

    return output


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))
