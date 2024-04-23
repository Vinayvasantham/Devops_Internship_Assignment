import logging
import signal
import sys
import re
import time
from collections import Counter

# Configure logging
logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to handle Ctrl+C signal
def signal_handler(sig, frame):
    logging.info("Monitoring stopped.")
    sys.exit(0)

# Function to perform basic log analysis
def analyze_log(log_file):
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
            error_count = 0
            error_messages = {}
            http_status_codes = Counter()
            for line in lines:
                if "Error" in line:
                    error_count += 1
                    message = line.strip()
                    if message in error_messages:
                        error_messages[message] += 1
                    else:
                        error_messages[message] = 1
                # Extract HTTP status codes (assuming they are in the format "HTTP <status_code>")
                match = re.search(r'HTTP\s+(\d+)', line)
                if match:
                    status_code = match.group(1)
                    http_status_codes[status_code] += 1

            # Log total number of errors
            logging.info(f"Total number of errors: {error_count}")

            # Log top error messages
            if error_count > 0:
                logging.info("Top error messages:")
                sorted_errors = sorted(error_messages.items(), key=lambda x: x[1], reverse=True)
                for error, count in sorted_errors[:5]:  # Display top 5 error messages
                    logging.info(f"{error} - Count: {count}")

            # Log HTTP status codes occurrences
            logging.info("HTTP status codes:")
            for code, count in http_status_codes.items():
                logging.info(f"HTTP {code} - Count: {count}")

    except FileNotFoundError:
        logging.error(f"Log file '{log_file}' not found.")
        sys.exit(1)

# Function to monitor log file for new entries
def monitor_log_file(log_file):
    try:
        with open(log_file, 'r') as file:
            while True:
                new_line = file.readline()
                if new_line:
                    logging.info(new_line.strip())  # Log the new line
                else:
                    time.sleep(0.1)  # Sleep briefly before checking for new lines
    except FileNotFoundError:
        logging.error(f"Log file '{log_file}' not found.")
        sys.exit(1)

# Main function
def main():
    if len(sys.argv) != 2:
        logging.error("Usage: python monitor.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    logging.info(f"Monitoring log file '{log_file}'. Press Ctrl+C to stop.")

    # Perform log analysis
    analyze_log(log_file)

    # Start monitoring the log file
    monitor_log_file(log_file)

if __name__ == "__main__":
    main()