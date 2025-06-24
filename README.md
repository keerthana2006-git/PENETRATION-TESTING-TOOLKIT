# PENETRATION-TESTING-TOOLKIT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KEERTHANA SASIKUMAR

*INTERN ID*: CT04DF1796

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION OF PENETRATION TESTING TOOLKIT*
The Penetration Testing Toolkit is a Python-based command-line application designed to simulate essential ethical hacking techniques and security practices.
It includes:-
-> PORT SCANNING:  1) Scans a list of common ports (21, 22, 23, 25, 80, 443, 3306) on a given IP address.  2) Helps identify which services might be running on the target system.
-> BANNER GRABBING: 1) Connects to each open port and tries to read the service banner.  2) Banners often contain version info, which helps identify possible vulnerabilities.
-> SERVICE DETECTION: 1) Maps common ports to known services like HTTP, FTP, SSH, etc.  2) Helps quickly identify the nature of services running on open ports
-> VULNERABILITY CHECKING: 1) Matches retrieved service banners against a small database of known vulnerable versions.  2) Alerts the user if any known vulnerability is detected.
-> HTTP BRUTE-FORCE LOGIN TESTING: 1) Prompts the user for a login URL and username.  2) Tries a list of common passwords to brute-force login access.

Note:-  The brute force works perfectly only with a Flask-based test login page.

TECHNOLOGIES USED:
1) Python 3
2)Socket programming (for scanning & banner grabbing)
3)Requests library (for HTTP brute-force)
4)Flask (for local testing)

HOW IT'S USED:
1)Enter a target IP (e.g., 127.0.0.1)
2)Tool scans common ports
3)For each open port:
->Grabs banner
->Detects service
->Checks known vulnerabilities
4)Optionally brute-forces a login form (HTTP POST)

APPLICATIONS OF THE PENETRATION TESTING TOOLKIT:
1. Ethical Hacking & Security Audits:- This toolkit can be used by ethical hackers to perform initial reconnaissance on a network or system. Features like port scanning, banner grabbing, and service detection help identify open services and potential entry points during a security assessment.
2. Vulnerability Assessment:- By matching service banners to known vulnerable versions, the toolkit aids in identifying common misconfigurations and outdated software, helping administrators patch issues before they can be exploited.
3. Web Application Testing:- The HTTP brute-force module is useful for testing the strength of login mechanisms in web applications. It helps security teams evaluate if user accounts are vulnerable to brute-force attacks and whether rate limiting or account lockout mechanisms are in place.
4. Cybersecurity Education & Training:- This tool is highly effective in academic and lab environments for teaching students about basic penetration testing techniques. The included mock login server allows learners to safely test brute-force attacks without impacting real systems.
5. CTF (Capture The Flag) Practice:- The toolkit can be used in CTF competitions and practice labs where participants must identify open ports, detect services, and exploit weak credentials to gain access.
6. Internal Network Scanning:- Organizations can use this tool within their own internal networks to simulate attacker behavior, helping them proactively identify weaknesses in exposed services or authentication mechanisms.
7.  Internship & Research Projects:- For students and interns, the toolkit serves as an ideal project to demonstrate understanding of real-world cybersecurity concepts, showcasing skills in Python, networking, and penetration testing methodologies.

#IMPORTANT NOTE# 
DO NOT RUN THIS TOOLKIT ON ANY SYSTEMS OR SERVER UNLESS YOU HAVE EXPLICIT PERMISSION FROM THE OWNER!!!

Running port scans, brute-force attacks, or vulnerability checks on websites, public IP's, corporate servers, even other people's devices without permission is considered unauthorized access, and it can be illegal under cybersecurity laws.

Thus, only run on the systems you own or have permission to test...!!!

#OUTPUT

![Image](https://github.com/user-attachments/assets/70a4e1e1-4269-4bbc-957a-94568ed34721)
![Image](https://github.com/user-attachments/assets/0f827e83-86c0-4d74-a4bc-ac3d155cf9c5)



















