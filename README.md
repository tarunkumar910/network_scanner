# Network Scanner Tool

<p align="center">
  <a href="#introduction">Introduction</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#working">Working</a> •
  <a href="#future-enhancements">Future Enhancements</a> •
  <a href="#disclaimer">Disclaimer</a>
</p>

---

## Introduction

The **Network Scanner Tool** is a Python-based utility that uses the `Scapy` library to scan an IP range or a single IP address and retrieve the MAC addresses associated with them. This tool helps in identifying devices on the local network and gathering essential information for network management or penetration testing tasks.

---

## Features

- **IP Range Scanning**: Scan a given IP range or a single IP address.
- **MAC Address Detection**: Automatically retrieves the MAC address for each IP address in the scan.
- **Formatted Output**: Displays the IP and MAC addresses in a clean and readable format.
- **Simple Command-Line Interface**: Easily configurable through the terminal with command-line arguments.

---

## Installation

### Prerequisites

To run this project, you need:

- **Python**: Version 3.6 or higher.
- **Scapy Library**: Install it using pip:
  ```bash
  pip install scapy
  ```

### Steps to Install
  ```bash
git clone https://github.com/your-repo/network-scanner.git
cd network-scanner
pip install -r requirements.txt
  ```
## Working
- ARP Request: The script sends ARP requests to each IP in the given range or to the single IP provided.
- MAC Address Retrieval: It collects the MAC address associated with each responding IP address.
- Formatted Output: The script displays the IP addresses and their corresponding MAC addresses in a readable table format.



## Future Enhancements
- Add the ability to save scan results to a file (CSV or JSON).
- Implement a more detailed scan with device information (OS, vendor, etc.).
- Add multi-threading for faster scanning on large networks.
- Improve error handling for edge cases (invalid IP range, unreachable hosts).


## Disclaimer
This tool is for educational purposes only. Unauthorized scanning or accessing devices on a network without consent can be illegal. Use responsibly and ensure you have permission to scan the network.

### Key Sections:
1. **Introduction**: A brief overview of the project and its purpose.
2. **Features**: Describes the features of the Network Scanner tool.
3. **Installation**: Lists the prerequisites and steps for setting up the project.
4. **Usage**: Explains how to run the tool with different arguments.
5. **Working**: Provides an explanation of the main functionality behind the tool.
6. **Future Enhancements**: Lists possible improvements that could be made to the tool.
7. **Disclaimer**: Reminder to use the tool responsibly.

This structure should help users quickly understand what the project is about and how to use it.




  
