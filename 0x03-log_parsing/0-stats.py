#!/usr/bin/python3

""" a script that reads stdin line by line and computes metrics """
import sys
from collections import defaultdict

# initialize variables
total_size = 0
status_code_counts = defaultdict(int)
line_count = 0

# process input line by line
for line in sys.stdin:
    line = line.strip()

    # parse input line
    try:
        ip, _, _, date, request, status_code, file_size = line.split()
        if request != 'GET /projects/260 HTTP/1.1':
            continue
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        continue

    # update metrics
    total_size += file_size
    status_code_counts[status_code] += 1
    line_count += 1

    # print statistics every 10 lines or on keyboard interruption
    if line_count % 10 == 0:
        print(f"Total file size: {total_size}")
        for status_code in sorted(status_code_counts):
            print(f"{status_code}: {status_code_counts[status_code]}")
        print("")

# print final statistics
print(f"Total file size: {total_size}")
for status_code in sorted(status_code_counts):
    print(f"{status_code}: {status_code_counts[status_code]}")
