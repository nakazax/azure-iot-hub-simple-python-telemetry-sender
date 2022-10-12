# Azure IoT Hub Simple Python Telemetry Sender
This repository includes a Python script that sends dummy telemetry to Azure IoT Hub. The telemetry format is based on [Raspberry Pi Azure IoT Online Simulator](https://azure-samples.github.io/raspberry-pi-web-simulator/), and includes `messageId`, `deviceId`, `temperature` and `humidity`.

## Prerequisites
This script depends on `azure-iot-device`, etc. The dependent libraries are listed in requirements.txt. Please install the dependent libraries by the following command.

```
$ pip3 install -r requirements.txt
```

## Usage
```
$ python3 ./azure-iot-hub-simple-python-telemetry-sender/apps/sender.py --connection-string
                                                                        [--interval-seconds]
                                                                        [--message-id]
```

- `--connection-string` (Required): Connection string for the IoT Hub.
- `--interval-seconds` (Optional): Interval in seconds between sending messages. Default is `10` seconds.
- `----message-id` (Optional): Starting message ID. Default is `1`.

### Optional: Background execution (for Linux)
If backgroud execution is preffered, run the command with `nohup`.

```
nohup python3 ./azure-iot-hub-simple-python-telemetry-sender/apps/sender.py --connection-string "HostName=example.azure-devices.net;DeviceId=myDeviceId;SharedAccessKey=xxx" > /dev/null 2>&1 &
```
