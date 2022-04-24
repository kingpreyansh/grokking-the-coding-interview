# coding: utf-8
# Problem: We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.
# Jobs: [[1,4,3], [2,5,4], [7,9,6]]
# Output: 7
# Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the
# jobs are running at the same time i.e., during the time interval (2,4).
# Leetcode Equivalent: None
# Optimal solution:

def maximum_CPU_load(jobs):


if __name__ == "__main__":
    jobs = [[1, 4, 3], [2, 5, 4], [7, 9, 6]]
    print(maximum_CPU_load(jobs))
