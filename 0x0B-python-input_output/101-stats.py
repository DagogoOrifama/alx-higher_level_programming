import sys
from collections import defaultdict

# Initialize variables
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    # Read lines from standard input
    for line in sys.stdin:
        # Parse input data
        parts = line.strip().split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: File size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    # Print final statistics on keyboard interrupt
    print(f"Total file size: File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
