To extend the manual log review I wrote a Python script to automatically scan Linux log files for suspicious activity (failed logins,
unknown users, etc.)
The Python script opens the Linux_2k.log file and reads its lines into a list called logs.
It then takes lines 200 to 500 and puts them in a new list, subset_logs. The script checks each line in this subset for keywords like 
"Failed password" "authentication failure" and "user unknown" or "invalid user." Any matching line is added to a list called suspicious_entries 
with a tag for the event type (like “Failed Login”). The script prints these flagged entries and shows the total number of suspicious events found. 
This automates scanning log lines to quickly identify suspicious activity that would otherwise require manual review.

After I ran my Python file I exported the results to a CSV file.
