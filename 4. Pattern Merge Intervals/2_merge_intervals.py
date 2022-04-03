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
    # sort the array according to what we need
    intervals.sort(key=lambda x: x[0])
    # want the first element in the intervals array
    result = [intervals[0]]
    # iterate through the intervals starting from 2nd element as the 1st is in the result array
    for start, end in intervals[1:]:
        # get the last element's last value
        lastEnd = result[-1][1]
        # if the start of the new element being added is smaller than the end of the last item added
        if start <= lastEnd:
            # it means that it overlaps and we can get the max of the two intervals' ends to add
            result[-1][1] = max(end, lastEnd)
        else:
            # if it doesnt overlap add as a non overlapping interval
            result.append([start, end])
    return result


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))
