This objective is about analyzing computer logs to identify suspicious login
activity. I will identify failed login attempt in a real world log file.
This dataset simulates real-world Linux system logs, including authentication attempts,
user sessions, and system events.

Firstly, I dowloaded Linux_2k.log from LogHub Linux logs. 

To keep the project manageable, I analyzed a sections lines of the log file.
In this case, VS Code was utilized to help track the first 20 to 40 lines.

Looking at the log entries I checked for any signs of failes logins or unusual activity. These signs could be:

● Repeated failed logins from the same IP address.

● Unknown or invalid users are attempting to log in.

● System alerts or abnormal exits that suggest possible issues. 


<img width="1028" height="353" alt="logs" src="https://github.com/user-attachments/assets/48590848-5121-486f-ba2f-6d00921fa24f" />


The logs indicate several failed login attempts from the IP addresses 218.188.2.4 and
220.135.151.1, mainly targeting the root account. This strongly suggests the possibility
of brute-force attack attempts. The repeated failures from these specific IP addresses
indicate either automated attacks or probing activities. Additionally, the presence of
"user unknown" messages shows that attackers are randomly trying various usernames.
Moreover, the event labeled "ALERT exited abnormally" suggests there may be an
underlying system issue that requires further investigation.



