# coding: utf-8
# Problem: Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.
# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
# Leetcode Equivalent: https://leetcode.com/problems/meeting-rooms-ii/
# Optimal solution: O(NlogN)

def minMeetingRooms(intervals):
    # Algorithm:

    # build an array with both the start times and the end times
    start = sorted([item[0] for item in intervals])
    end = sorted([item[1] for item in intervals])

    # the indices and to track the max counters
    s, e = 0, 0
    res, count = 0, 0

    # iterate through both the arrays and count up
    while s < len(start) and e < len(end):
        if start[s] < end[e]:
            # move pointer up if a meeting has started but not ended yet
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        # get the max
        res = max(res, count)
    return res


if __name__ == "__main__":
    intervals = [[1, 4], [2, 5], [7, 9]]
    print(minMeetingRooms(intervals))
