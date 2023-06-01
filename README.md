# PortScanner

The Python Port Scanner is a command-line tool written in Python that allows users to scan for open ports on a target host. It provides two options for scanning:

1. Scan the first 1000 ports: This option scans the most commonly used ports to quickly identify any open ports and associated services.
2. Scan all ports: This option scans all 65,535 ports to perform a comprehensive scan and identify any open ports.

The port scanner utilizes the `python-nmap` module to perform the scanning functionality.

## Features
- Scans for open ports on a target host.
- Provides options to scan the first 1000 ports or all ports.
- Utilizes the `python-nmap` module for efficient scanning.

## Requirements
- Python 3.x
- `python-nmap` module

## Usage
1. Clone this repository or download the source code files.
2. Open a terminal or command prompt and navigate to the directory where the Port Scanner files are located.
3. Install the `python-nmap` module by running the following command:
   ```
   pip install python-nmap
   ```
4. Run the Port Scanner with the following command:
   ```
   python port_scanner.py [target_host]
   ```
   
   Replace `[target_host]` with the IP address or hostname of the target host you want to scan.
   
   Example:
   ```
   python port_scanner.py 192.168.0.1
   ```
5. Follow the displayed instructions to either scan furst 1000 ports or all 65535 ports
5. The Port Scanner will start scanning the specified target host based on the chosen option.
6. Once the scan is complete, the tool will display the results, showing which ports are open.

**Note:** Please ensure that you have proper authorization before scanning any hosts. Unauthorized port scanning can be a violation of network security policies or even illegal in certain cases.

## License
This project is licensed under the [MIT License](LICENSE).

## Disclaimer
The Python Port Scanner is provided as-is without any guarantee or warranty. Use it responsibly and at your own risk. The developers are not responsible for any misuse or damage caused by the tool.
