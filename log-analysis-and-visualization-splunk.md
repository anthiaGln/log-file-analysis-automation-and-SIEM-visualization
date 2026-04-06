Building on the manual and automated log analysis, this objective introduces
Splunk, a Security Information and Event Management (SIEM) tool used in
professional SOC environments.

On the splunk I uploaded the Linux_2k.log file. In order to sreach the log for suspicious activity I used the query
default_metadata (“Failed password” or “authentication failure” OR “invalid user” OR “user unknown”)

This filters the log to show only entries that match common indicators of brute-force
attempts or unauthorized access, such as:

● Repeated failed logins

● Invalid or unknown users

● Authentication failures

With reviewing these results we can identify patterns in timestamps, usernames, and IP
addresses.

After running the search query, Splunk shows all matching log entries under the Events
tab.

One entry immediately stands out:

● Repeated failed login attempts

● Same username attempted: root

● Same source IP: 207.243.167.114

● Attempts occur within very short intervals (a few seconds apart)


<img width="557" height="298" alt="Στιγμιότυπο οθόνης 2026-03-21 181656" src="https://github.com/user-attachments/assets/1e1c6319-a6fc-4083-9b83-2ecbb68d0966" />
