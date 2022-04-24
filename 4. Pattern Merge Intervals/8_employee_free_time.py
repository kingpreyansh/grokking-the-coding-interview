# coding: utf-8
# Problem: For ‘K’ employees, we are given a list of intervals representing the working hours of each employee. Our goal is to find out if there is a free interval that is common to all employees. You can assume that each list of employee working hours is sorted on the start time.
# Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
# Output: [3,5]
# Explanation: Both the employess are free between [3,5].
# Leetcode Equivalent:
# Optimal solution:

def employee_free_time(jobs):


if __name__ == "__main__":
    jobs = [[[1, 3], [5, 6]], [[2, 3], [6, 8]]]
    print(employee_free_time(jobs))
