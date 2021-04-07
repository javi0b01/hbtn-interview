#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ Returns a list of lists of integers
    representing the Pascal's triangle of n """
    aList = [[] for i in range(0, n)]
    for row in range(0, n):
        for column in range(row+1):
            if ( column < row):
                if (column <= 0):
                    aList[row].append(1)
                else:
                    aList[row].append(aList[row - 1][column] +
                    aList[row - 1][column - 1])
            elif (row == column):
                aList[row].append(1)
    return (aList)
