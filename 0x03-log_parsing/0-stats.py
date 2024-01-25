#!/usr/bin/python3
import sys
from collections import defaultdict


def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))


def process_line(line, total_size, status_counts):
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        total_size += file_size

        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_counts[status_code] += 1

        return total_size, status_counts

    except (ValueError, IndexError):
        return total_size, status_counts


total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        total_size, status_counts = process_line(
            line.strip(), total_size, status_counts)

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)