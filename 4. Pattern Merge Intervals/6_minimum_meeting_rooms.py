# coding: utf-8
# Problem: Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.
# Meetings: [[1,4], [2,5], [7,9]]
# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can
# occur in any of the two rooms later.
# Leetcode Equivalent: Not there
# Optimal solution:

def minimum_meeting_rooms(meetings):
    # Algorithm:
    # 1) make two different lists 1. for the starts and 2. for the ends
    # 2) keep a count of the max amount of meetings that are going on at once
    # 3) return the max
    start = sorted([item[0] for item in meetings])
    end = sorted([item[1] for item in meetings])
    s, e = 0, 0
    maxCount, count = 0, 0
    for i in range(len(meetings)):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        maxCount = max(maxCount, count)

    return maxCount


if __name__ == "__main__":
    meetings = [[1, 4], [2, 5], [7, 9]]  # [1, 2, 7], [4, 5, 9]
    print(minimum_meeting_rooms(meetings))
