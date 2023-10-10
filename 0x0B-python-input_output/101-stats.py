#!/usr/bin/python3
"""
Module: 101-stats
Reads stdin line by line and computes metrics.
"""
import sys


def print_metrics(total_size, status_codes):
    """
    Prints the metrics: total file size and number of lines by status code.

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary containing the count of each
                                status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """
    Parses a line and extracts the file size and status code.

    Args:
        line (str): The input line.

    Returns:
        tuple: A tuple containing the file size (int) and status code (str).
    """
    parts = line.split()
    size = int(parts[-1])
    code = parts[-2]
    return size, code


def main():
    """
    Main function that reads stdin line by line and computes metrics.
    """
    total_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            size, code = parse_line(line)
            total_size += size
            if code in status_codes:
                status_codes[code] += 1

            if count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
