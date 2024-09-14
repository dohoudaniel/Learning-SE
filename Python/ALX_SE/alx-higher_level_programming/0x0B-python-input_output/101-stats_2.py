#!/usr/bin/python3
import sys

def compute_metrics():
    """Reads stdin line by line and computes metrics."""

    # Initialize variables
    total_size = 0
    status_codes = {}

    try:
        # Read lines from stdin
        for line_number, line in enumerate(sys.stdin, 1):

            # Parse the line and extract the file size and status code
            _, _, _, _, status_code, file_size = line.split()

            # Update the total file size
            total_size += int(file_size)

            # Update the count for the status code
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            # Print statistics every 10 lines
            if line_number % 10 == 0:
                print("Total file size:", total_size)
                for code in sorted(status_codes.keys()):
                    print(code + ":", status_codes[code])

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print("Total file size:", total_size)
        for code in sorted(status_codes.keys()):
            print(code + ":", status_codes[code])

if __name__ == "__main__":
    compute_metrics()
