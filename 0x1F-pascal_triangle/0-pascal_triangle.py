#!/usr/bin/python3
""" Pascal's Triangle """
def pascal_triangle(n):
    """ Returns a list of lists of integers
        representing the Pascal's triangle of n """
    aList = [[] for i in range(0, n)]
    for row in range(0, n):
        for col in range(row+1):
            if ( col < row):
                if (col <= 0):
                    aList[row].append(1)
                else:
                    aList[row].append(aList[row - 1][col] + aList[row - 1][col - 1])
            elif (row == col):
                aList[row].append(1)
    return (aList)
