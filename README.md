# Flow-Log-Tagging

This program processes flow log data, maps each row to a tag based on a lookup table, and generates statistics on the number of matches for each tag and port/protocol combination. The program supports large log files and uses a CSV lookup table to determine the correct tag for each flow log entry.

# Features
1. Parse flow logs in AWS VPC flow log format (version 2).
2. Map flow logs to tags using a CSV-based lookup table.
3. Generate counts for tags and port/protocol combinations.
4. Supports case-insensitive matching for tags and protocols.
5. Efficient handling of flow logs up to 10 MB and lookup tables with up to 10,000 mappings.

# Requirements
1. Python 3.6 or higher.
2. Input flow log file (flow_logs.txt).
3. Input lookup table file (lookup_table.csv).

# Assumptions
1. Log Type and Version: The program assumes the flow log data follows AWS VPC flow logs format, specifically version 2.
2. Protocol Codes: Flow logs use numeric protocol codes, such as 6 for TCP, 17 for UDP, 1 for ICMP.
3. Empty Rows: Any row that is empty or contains only whitespace is ignored.
4. Missing Data: Rows with missing fields are skipped, and a warning is displayed.

# Compilation and Running the Program
This is a Python-based script, so there is no compilation step required. You only need to execute the program directly.You can run the program using the following command:
```
python flow_log_parser.py
 ```

# Tests

# Test Setup
1. Flow log file: A sample flow log file (flow_log.txt) that contains network data in AWS VPC flow log version 2 format.
2. Lookup table: A sample CSV file (lookup_table.csv) that contains mappings of port, protocol, and corresponding tags.

# Tests Performed:
1.Basic Flow Log Parsing: The program was tested with flow logs containing various entries, including:
- Logs with matching port/protocol combinations.
- Logs with unmatched entries (tagged as "Untagged").
2. Case-Insensitive Matching: The lookup table matches tags correctly regardless of case, both for protocols (e.g., TCP, tcp) and tags (e.g., sv_P1, SV_P1).
3. Handling Missing Data: The program was tested with incomplete rows (e.g., missing protocol or port) to ensure they are skipped properly with warnings displayed.
4. Efficiency: The program was tested with flow log files up to 10 MB in size, processing each log entry without significant delays.
  
# Edge Cases:
1. Empty Lines: Lines that are empty or only contain whitespace are ignored.
2. Invalid Format: Rows with missing fields or invalid data are skipped, and a warning is logged.
3. Large Input Size: The program handled input files up to 10 MB without issue, keeping performance optimized.
