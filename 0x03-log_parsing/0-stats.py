#!/usr/bin/python3
''' A script that reads from stdin and produces stats '''
import sys

# Initialize counters for file size and status codes
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    # Read input from stdin line by line
    for i, line in enumerate(sys.stdin):
        # Parse the line to extract the file size and status code
        try:
            _, _, _, _, _, status, size = line.split()
            status = int(status)
            size = int(size)
        except ValueError:
            # If the line doesn't match the expected format, skip it
            continue

        # Update counters
        total_size += size
        if status in status_codes:
            status_codes[status] += 1

        # Print statistics after every 10 lines
        if (i + 1) % 10 == 0:
            print(f'Total file size: {total_size}')
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f'{code}: {count}')
            print('-' * 10)
except KeyboardInterrupt:
    # Print final statistics on keyboard interruption
    print(f'Total file size: {total_size}')
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f'{code}: {count}')
