#!/bin/bash

# Specify the path to the test log file
LOG_FILE="/var/log/test.log"

# Monitor the log file in real-time using tail
tail -f "$LOG_FILE"
