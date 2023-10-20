#!/usr/bin/python3
"""log parsing"""


import sys


def print_stats(status_codes, file_size):
    """print stats"""
    print("File size: {}".format(file_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    counter = 0
    try:
        for line in sys.stdin:
            counter += 1
            data = line.split(" ")
            if len(data) > 2:
                file_size += int(data[-1])
                if data[-2] in status_codes:
                    status_codes[data[-2]] += 1
            if counter % 10 == 0:
                print_stats(status_codes, file_size)
    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise
    print_stats(status_codes, file_size)
