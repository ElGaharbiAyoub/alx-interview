#!/usr/bin/python3
""" Log parsing """
import sys
from collections import defaultdict


def print_metrics(total_file_size, status_code_counts):
    """Print the metrics"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts):
        count = status_code_counts[code]
        if count > 0:
            print('{}: {}'.format(code, count))


total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        try:
            status_code = int(parts[-2])
            status_code_counts[status_code] += 1
        except Exception as err:
            pass

        try:
            file_size = int(parts[-1])
            total_file_size += file_size
        except Exception as err:
            pass

        if line_count % 10 == 0:
            print_metrics(total_file_size, status_code_counts)
finally:
    print_metrics(total_file_size, status_code_counts)
