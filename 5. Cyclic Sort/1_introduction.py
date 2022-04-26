# coding: utf-8
# When to use: This pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range.
# Example Problem: You are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means that some numbers will be missing. Find all the missing numbers.
# Solution/Algorithm:
# 1) We can try placing each number in its correct place, i.e., placing ‘1’ at index ‘0’, placing ‘2’ at index ‘1’, and so on.
# 2) Once we are done with the sorting, we can iterate the array to find all indices that are missing the correct numbers.
#
