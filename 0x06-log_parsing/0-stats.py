#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
if __name__ == '__main__':
    import sys

    def print_results(statusCodes, fileSize):
        """ Print statistics """
        print("File size: {:d}".format(fileSize))
        for statusCode, times in sorted(statusCodes.items()):
            if times:
                print("{:s}: {:d}".format(statusCode, times))
    n_lines = 0
    statusCodes = {"200": 0,
                   "301": 0,
                   "400": 0,
                   "401": 0,
                   "403": 0,
                   "404": 0,
                   "405": 0,
                   "500": 0
                   }
    fileSize = 0
    try:
        """ Read stdin line by line """
        for line in sys.stdin:
            n_lines += 1
            data = line.split()
            try:
                """ Compute metrics """
                statusCode = data[-2]
                if statusCode in statusCodes:
                    statusCodes[statusCode] += 1
                fileSize += int(data[-1])
            except:
                pass
            if n_lines % 10 == 0:
                """ After every 10 lines, print from the beginning """
                print_results(statusCodes, fileSize)
        print_results(statusCodes, fileSize)
    except KeyboardInterrupt:
        """ Keyboard interruption, print from the beginning """
        print_results(statusCodes, fileSize)
        raise

