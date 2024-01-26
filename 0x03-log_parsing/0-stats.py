#!/usr/bin/python3
""" Log parsing """
import sys
from collections import defaultdict


def print_stats(total_size, status_counts):
    """ Print stats """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))


def process_line(line, total_size, status_counts):
    """ Process a line from stdin """
    parts = line.split()
    try:
        status_code = int(parts[-2])

        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_counts[status_code] += 1

    except (ValueError, IndexError):
        pass

    try:
        file_size = int(parts[-1])

        total_size += file_size

    except (ValueError, IndexError):
        pass

    return total_size, status_counts


total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        total_size, status_counts = process_line(
            line, total_size, status_counts)

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

finally:
    print_stats(total_size, status_counts)
