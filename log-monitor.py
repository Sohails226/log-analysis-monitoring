#!/usr/bin/env python3

import time

# Specify the path to the test log file
LOG_FILE = "/var/log/test.log"

# Main function for monitoring and analysis
def monitor_log():
    while True:
        with open(LOG_FILE, 'r') as file:
            # Read all new lines since the last read position
            new_lines = file.readlines()
            # Process new log entries (perform analysis here)
            for line in new_lines:
                # Example: Count occurrences of keyword 'error'
                if 'error' in line.lower():
                    print("Error found:", line.strip())
        time.sleep(1)  # Wait for 1 second before checking for new entries

if __name__ == "__main__":
    monitor_log()
