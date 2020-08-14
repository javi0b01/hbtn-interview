#!/usr/bin/python3
""" In a text file, there is a single character H.  Your text editor can
execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file. """


def minOperations(n):
    n_operations = 0
    min_op = 2
    while n > 1:
        while n % min_op == 0:
            n_operations += min_op
            n /= min_op
        min_op += 1
    return n_operations

