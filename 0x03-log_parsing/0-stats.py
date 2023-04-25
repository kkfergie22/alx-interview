#!/usr/bin/python3

"""
This script reads lines of input from standard input and computes
metrics based on the input format. The format
should be in the following format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

The script prints statistics every 10 lines or on keyboard interruption.
The statistics include the total file size and the number of lines by
status code, where possible status codes are 200, 301, 400, 401,
403, 404, 405, and 500.
Status codes that do not appear or are not integers will not be printed

Example usage:

$ cat input.txt | python my_script.py
"""


import sys
from collections import defaultdict
from typing import Dict, Any

# initialize variables
total_size: int = 0  # total file size
status_code_counts: Dict[int, int] = defaultdict(
    int)  # number of lines by status code
line_count: int = 0  # count of processed lines

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
    except ValueError:  # skip if the line is not in the expected format
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
