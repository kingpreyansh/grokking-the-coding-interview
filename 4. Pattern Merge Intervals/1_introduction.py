# coding: utf-8
# When to use: This pattern describes an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if they overlap.
# Example Problem: Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
# Solution/Algorithm:
# 1) Sort by start value of the intervals
# 2) Iterate through the array of intervals
# 3) If it overlaps then merge the intervals
