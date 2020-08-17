#!/usr/bin/python3
""" In a text file, there is a single character H.  Your text editor can
execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file. """


def minOperations(n):
    """ Method that calculates number of operations needed """
    if type(n) != int:
        return 0
    minOpe = 2
    nOpe = 0
    while n >= minOpe:
        if not (n % minOpe):
            n = int(n / minOpe)
            nOpe += minOpe
            minOpe = 1
        minOpe += 1
    return nOpe

