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

<img width="557" height="298" alt="Στιγμιότυπο οθόνης 2026-03-21 181656" src="https://github.com/user-attachments/assets/1e1c6319-a6fc-4083-9b83-2ecbb68d0966" />

After running the search query, Splunk shows all matching log entries under the Events
tab.

One entry immediately stands out:

● Repeated failed login attempts

● Same username attempted: root

● Same source IP: 207.243.167.114

● Attempts occur within very short intervals (a few seconds apart)

This behavior is highly consistent with brute-force login attempts, so we follow this IP
deeper through the visualization tools.

● Events View – Identifying the Suspicious Source

<img width="560" height="274" alt="identify suspicious source" src="https://github.com/user-attachments/assets/e036afbf-c11e-4a9b-a0be-eff04defb7fb" />

In the Events view the IP 207.243.167.114 appears multiple times attempting to log into root.

This raises a red flag because:

● “root” is a high-value target

● Repeated failures indicate likely unauthorized access attempts

At this point, we should escalate this for pattern analysis.

● Patterns View — Confirming Repetitive Behavior

Switching to Patterns, Splunk clusters similar events.


<img width="557" height="219" alt="patterns view" src="https://github.com/user-attachments/assets/7bc8a1f9-5987-4bc7-9a37-b2a8b839270c" />


One pattern appears prominently:

● “Failed password for root”

This confirms that multiple source IP generated repeated failures using the same
target account. 

Statistics View – Breaking Down the Data

Switch to the Statistics tab to group events by IP, user, and event count.
Observations include:

● 150.183.249.110 has the highest number of event count

● Targeted username is consistently root

● Other IPs show fewer and scattered attempts

This tabular view provides clarity on the scale and focus of the attack.

<img width="546" height="275" alt="statistics view" src="https://github.com/user-attachments/assets/8977b626-ef3a-418c-a27e-c95e05052c9e" />

