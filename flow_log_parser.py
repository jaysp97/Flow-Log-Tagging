import csv
from collections import defaultdict

# Define file paths
FLOW_LOG_FILE = 'flow_logs.txt'  # Flow logs in txt format
LOOKUP_TABLE_FILE = 'lookup_table.csv'  # Lookup table CSV file
OUTPUT_FILE = 'output_counts.csv'  # Output CSV file for the counts

def load_lookup_table(filename):
    """Load the lookup table from a CSV file."""
    lookup = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            dstport = row[0].strip()
            protocol = row[1].strip().lower()
            tag = row[2].strip()
            lookup[(dstport, protocol)] = tag
    return lookup

def parse_flow_logs(filename, lookup_table):
    """Parse the flow logs and map each row to a tag based on the lookup table."""
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    PROTOCOL_MAP = {
        '6': 'tcp',
        '17': 'udp',
        '1': 'icmp',
    }

    with open(filename, mode='r') as file:
        for line in file:
            # Skip empty or whitespace-only lines
            if not line.strip():
                continue

            # Split line into components (assuming space-separated values)
            row = line.split()

            # Ensure we are getting the right indices for dstport and protocol
            if len(row) < 8:
                print(f"Skipping line due to insufficient fields: {line}")
                continue  # Skip lines that do not have enough data
            
            dstport = row[5].strip()
            protocol = row[7].strip().lower()
            # Convert protocol code to string (tcp, udp, etc.)
            protocol = PROTOCOL_MAP.get(protocol, protocol.lower())

            # Find the matching tag based on dstport and protocol
            tag = lookup_table.get((dstport, protocol), "Untagged")
            tag_counts[tag] += 1

            # Update the port/protocol combination count
            port_protocol_counts[(dstport, protocol)] += 1

    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, filename):
    """Write the output of tag counts and port/protocol counts to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write Tag Counts
        writer.writerow(["Tag Counts:"])
        writer.writerow(["Tag", "Count"])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])
        
        # Write Port/Protocol Combination Counts
        writer.writerow([])  # Blank line
        writer.writerow(["Port/Protocol Combination Counts:"])
        writer.writerow(["Port", "Protocol", "Count"])
        for (dstport, protocol), count in port_protocol_counts.items():
            writer.writerow([dstport, protocol, count])

def main():
    # Load the lookup table from the CSV file
    lookup_table = load_lookup_table(LOOKUP_TABLE_FILE)
    
    # Parse flow logs from the txt file and generate counts
    tag_counts, port_protocol_counts = parse_flow_logs(FLOW_LOG_FILE, lookup_table)
    
    # Write the output to a CSV file
    write_output(tag_counts, port_protocol_counts, OUTPUT_FILE)
    print(f"Output saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
