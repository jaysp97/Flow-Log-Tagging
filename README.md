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
2. Input flow log file (flow_log.txt).
3. Input lookup table file (lookup_table.csv).

# Assumptions
1. Log Type and Version: The program assumes the flow log data follows AWS VPC flow logs format, specifically version 2.
2. Protocol Codes: Flow logs use numeric protocol codes, such as 6 for TCP, 17 for UDP, 1 for ICMP.
3. Empty Rows: Any row that is empty or contains only whitespace is ignored.
4. Missing Data: Rows with missing fields are skipped, and a warning is displayed.
