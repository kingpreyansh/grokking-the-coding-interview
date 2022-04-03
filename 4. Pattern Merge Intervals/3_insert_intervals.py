# coding: utf-8
# Problem: Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
# Leetcode Equivalent: https://leetcode.com/problems/insert-interval/
# Optimal solution: O(NlogN)

def insert(intervals, newInterval):
    # appending the new interval into the set and then sorting it so we can use mergeInterval on it
    intervals.append(newInterval)
    intervals.sort(key=lambda x: x[0])

    # same as merging intervals that overlap
    result = [intervals[0]]
    for start, end in intervals[1:]:
        lastEnd = result[-1][1]
        if start <= lastEnd:
            result[-1][1] = max(lastEnd, end)
        else:
            result.append([start, end])
    return result


if __name__ == "__main__":
    intervals = [[1, 3], [5, 7], [8, 12]]
    print(insert(intervals, [4, 6]))
