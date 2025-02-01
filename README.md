# Pi-Status

A real-time Raspberry Pi system monitoring dashboard that provides essential system metrics through a clean web interface.

## Features

- Real-time CPU usage monitoring
- CPU temperature tracking
- Memory usage statistics
- Disk usage information
- Clean and responsive web interface
- Automatic data updates

## Prerequisites

- Python 3.x
- Raspberry Pi (or any Linux-based system)
- Web browser

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Pi-Status.git
   cd Pi-Status
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```
   
   If accessing from another device on your network, replace `localhost` with your Raspberry Pi's IP address.

## System Requirements

- Flask 3.0.0
- psutil 5.9.8

## How It Works

The application uses Flask as the web framework and psutil to gather system statistics. It provides two main endpoints:

- `/` - Serves the main dashboard interface
- `/stats` - JSON endpoint that provides real-time system statistics

The dashboard automatically updates every few seconds to show the latest system metrics.

## Notes

- CPU temperature monitoring requires access to system files (`/sys/class/thermal/thermal_zone0/temp`) or the `vcgencmd` utility
- The application runs on port 5000 by default
- Debug mode is enabled by default for development purposes

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.
