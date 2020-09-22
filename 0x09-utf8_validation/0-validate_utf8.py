#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding.
* Return: True if data is a valid UTF-8 encoding, else return False
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need to handle
* the 8 least significant bits of each integer
"""


def validUTF8(data):

    countBytes = 0
    for num in data:
        binNum = format(num, '#010b')[-8:]
        if countBytes == 0:
            for bit in binNum:
                if bit == '0':
                    break
                countBytes += 1
            if countBytes == 0:
                continue
            if countBytes == 1 or countBytes > 4:
                return False
        else:
            if not (binNum[0] == '1' and binNum[1] == '0'):
                return False
        countBytes -= 1
    return countBytes == 0

