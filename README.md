# EasyHub

EasyHub is a Python-based tool designed to track and display detailed task information and system usage statistics, helping you manage Windows resources efficiently. By leveraging the `psutil` library, EasyHub provides insights into CPU usage, memory usage, disk usage, and actively running tasks in real-time.

## Features

- **System Information:** Displays detailed system information including the OS, node name, release, version, machine, and processor.
- **CPU Usage:** Monitors and displays the current CPU utilization percentage.
- **Memory Usage:** Shows the total, available, used memory, and percentage usage.
- **Disk Usage:** Provides detailed disk usage statistics for each mounted device.
- **Task Information:** Lists all running processes with their PID, name, and username.

## Prerequisites

To run EasyHub, you need to have Python installed on your Windows system. Additionally, the following Python packages are required:

- `psutil`: For accessing system and process utilities.
- `tabulate`: For formatting output in a readable table format.

You can install these packages using pip:

```bash
pip install psutil tabulate
```

## Usage

To run EasyHub, execute the following command in your terminal:

```bash
python easyhub.py
```

Once started, EasyHub will continuously update and display system usage statistics and task information every 5 seconds.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributions

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue on the GitHub repository.

## Disclaimer

This tool is intended for educational and informational purposes only. Use it responsibly and at your own risk.