#!/usr/bin/python3
""" In a text file, there is a single character H.  Your text editor can
execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file. """


def minOperations(n):
    if type(n) != int or n < 1:
        return 0
    min_ope = 2
    if n == 1:
        return min_ope
    n_ope = 0
    while n > 1:
        while n % min_ope == 0:
            n_ope += min_ope
            n /= min_ope
        min_ope += 1
    return n_ope

