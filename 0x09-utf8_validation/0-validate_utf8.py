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
    bytesLong = 0
    for byte in data:
        binary = "{0:08b}".format(byte)
        if bytesLong == 0:
            for bit in binary:
                if bit == '0':
                    break
                bytesLong += 1
            if bytesLong == 0:
                continue
            if bytesLong == 1 or bytesLong > 4:
                return False
        else:
            if not (binary[0] == '1' and binary[1] == '0'):
                return False
        bytesLong -= 1
    return True

