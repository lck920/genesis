# Genesis Flood

🌪️ **What is this?**
A deluge of packets to test the resilience of the digital ark. Designed to generate significant traffic loads, it simulates high Gbps scenarios to push network infrastructures to their limits and evaluate resilience. When run concurrently across multiple instances, it can scale output to rigorously test capacity and bottleneck thresholds.

> [!WARNING]  
> **Disclaimer:** This tool is intended strictly for educational purposes, capacity planning, and testing networks that you own or have explicit, documented permission to test. Unauthorized use of this tool against targets without permission is illegal and strictly prohibited.

🚀 **Key Features**
- **Unlimited Capabilities**: Packed with multiple test modes (TCP, UDP, ICMP) to simulate diverse traffic patterns.
- **Stackable Power**: Designed to scale. Running multiple instances concurrently multiplies the generated traffic exponentially, allowing for extensive stress testing.
- **Resilience Evaluation**: Engineered to identify breaking points and test the failover or mitigation capabilities of target servers and networks.
- **Interactive Menu**: Easy-to-use console interface to select the protocol and parameters.
- **No External Dependencies**: Built entirely using Python's standard libraries (`socket`, `threading`, `os`, `struct`).

🛠️ **How to Use**
- **Python File**: This is a Python-based tool.
- **Easy Start**: You can simply double-click the file to run it, or open it via CMD (Command Prompt).
- Just select your test vector, set your parameters, and let Genesis Flood do the rest.

## Prerequisites

- **Python 3.x**: Ensure you have Python 3 installed on your system.
- **Administrator/Root Privileges**: Running ICMP floods requires administrative or root privileges due to the use of raw sockets.

## Installation

1. Clone this repository or download the source code:
   ```bash
   git clone https://github.com/lck920/genesis-flood
   cd genesis-flood
   ```

2. (Optional) While the script only relies on standard libraries, you can install the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script using Python:
   ```bash
   python3 main.py
   ```
   *Note: If you plan to use the ICMP flood feature on Linux/macOS, you must run the script with `sudo` (e.g., `sudo python3 main.py`). On Windows, run your Command Prompt or PowerShell as Administrator.*

2. You will be greeted with the Main Menu:
   - Select `1` to enter the Attack Menu.
   - Select `2` to Exit.

3. In the Attack Menu:
   - Select your desired protocol: TCP (1), UDP (2), or ICMP (3).
   - Enter the target IP address.
   - Select the desired thread count (Light, Medium, High, or Custom).
   - Enter the target port (for TCP and UDP).

4. The stress test will begin running in the background. Press `Enter` to return to the menu, and you can press `Ctrl+C` in your terminal to forcefully stop the script at any time.

> [!TIP]
> **Traffic Inspection**: It is highly recommended to use a network protocol analyzer like [Wireshark](https://www.wireshark.org/) alongside Genesis Flood to deeply inspect and analyze the network traffic generated during your tests.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## License

[MIT License](LICENSE)
