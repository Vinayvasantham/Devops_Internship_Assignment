This script automates the analysis and monitoring of log files. It continuously monitors a specified log file for new entries and performs basic log analysis, including counting occurrences of error messages and HTTP status codes.

Dependencies:
- Python 3.x

How to Use:

1.Clone the Repository:
- git clone <repository_link>

2.Navigate to the Directory:
- cd log-analysis-script

3.Run the Script:
- python log_monitor.py <log_file>
- Replace <log_file> with the path to the log file you want to monitor and analyze.

4.Testing:

- To test the script, you can create a sample log file with log entries similar to the provided example.
- Run the script with the sample log file and observe the output to ensure it meets the expected behavior.
  
Example:
- Suppose you have a log file named sample-logfile.log. To test the script, you can run:
- python log_monitor.py sample-logfile.log

Expected Output:

2024-04-23 09:00:00,001 - INFO - Monitoring log file 'sample-logfile.log'. Press Ctrl+C to stop.

2024-04-23 09:00:05,123 - INFO - New log entry: Error occurred: Unable to connect to database.

2024-04-23 09:00:10,456 - INFO - New log entry: HTTP 404 - Page not found.

2024-04-23 09:00:15,789 - INFO - New log entry: Error occurred: File not found.

2024-04-23 09:00:20,123 - INFO - New log entry: HTTP 500 - Internal server error.

2024-04-23 09:00:25,456 - INFO - New log entry: HTTP 404 - Page not found.
2024-04-23 09:00:30,789 - INFO - New log entry: Error occurred: Database connection timeout.
2024-04-23 09:00:35,123 - INFO - New log entry: Error occurred: Out of memory.
2024-04-23 09:00:40,456 - ERROR - Total number of errors: 4
2024-04-23 09:00:40,457 - ERROR - Top error messages:
2024-04-23 09:00:40,457 - ERROR - Error occurred: Unable to connect to database. - Count: 1
2024-04-23 09:00:40,457 - ERROR - Error occurred: File not found. - Count: 1
2024-04-23 09:00:40,457 - ERROR - Error occurred: Database connection timeout. - Count: 1
2024-04-23 09:00:40,457 - ERROR - Error occurred: Out of memory. - Count: 1
2024-04-23 09:00:40,789 - INFO - HTTP status codes:
2024-04-23 09:00:40,789 - INFO - HTTP 404 - Count: 2
2024-04-23 09:00:40,789 - INFO - HTTP 500 - Count: 1
Ensure that the script generates the expected output based on the log entries in the specified log file.
