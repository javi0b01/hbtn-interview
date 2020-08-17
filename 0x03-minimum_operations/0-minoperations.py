#!/usr/bin/python3
""" In a text file, there is a single character H.  Your text editor can
execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file. """


def minOperations(n):
    if n < 1:
        return 0
    min_op = 2
    if n == 1:
        return min_op
    n_operations = 0
    while min_op <= n:
        if not (n % min_op):
            n = int(n / min_op)
            n_operations += min_op
            min_op = 1
        min_op += 1
    return n_operations

