# log_analysis.py
# open and read log file
with open("Linux_2k.log", "r", encoding="utf-8") as file:
    logs = file.readlines()

# focus on lines 200–500
subset_logs = logs[199:500] # Python is 0-based index

# search for suspicious patterns
suspicious_entries = []
for line in subset_logs:
    if "Failed password" in line:
        suspicious_entries.append(("Failed Login", line.strip()))
    elif "authentication failure" in line:
        suspicious_entries.append(("Auth Failure", line.strip()))
    elif "user unknown" in line or "invalid user" in line:
        suspicious_entries.append(("Unknown User", line.strip()))

# Print Results
print("=== Suspicious Log Entries (Lines 200–500) ===")
for entry_type, entry in suspicious_entries:
    print(f"[{entry_type}] {entry}")

print(f"\nTotal suspicious entries found: {len(suspicious_entries)}")

# Save results to a CSV file
import csv
with open("suspicious_logs.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Type", "Log Entry"])
    writer.writerows(suspicious_entries)
print("Results saved to suspicious_logs.csv")
