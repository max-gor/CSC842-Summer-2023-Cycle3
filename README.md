# CSC842-Summer-2023-Cycle3

**PCAP FTP Finder**

One thing that differentiates programmers is being able to automate tasks. Network transfers may take a while to analyze, especially manually or visually. I wrote the program that would get through a PCAP file and find all FTP communications. The program would output captured usernames and passwords and would provide some statistical analysis on the FTP communications.

**Three main ideas:**
1.	Scapy is a great library that allows one to produce, alter and analyze network traffic.
2.	FTP is an insecure protocol that sends/receives login credentials in plain text.
3.	I know it is 2023, but FTP is still being widely used.

**Limitations and future work**
To be honest, I lost track of time and did not add some additional function such as file extraction, url/ip extraction and lookup. This program only shows a little glimpse into what can be done for automation of network traffic analysis.

**Running the program**
If you are planning to run the code, you can download it from the GitHub repository. You need to run it with python3 and enter a path to the PCAP file. Happy hunting for FTP passwords!
