# A script for sending Raspberry Pi simulated data to Azure IoT Hub
import argparse
import json
import random
import time

from azure.iot.device import IoTHubDeviceClient


def main(conn_str: str, message_id: int, interval_seconds: int) -> None:
    """Entry point for the application script"""
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    device_client.connect()
    while True:
        try:
            send_message(device_client, message_id)
            message_id += 1
            print(f"Waiting {interval_seconds} seconds...", flush=True)
            time.sleep(interval_seconds)
        except KeyboardInterrupt:
            print("Stopping script", flush=True)
            break
    device_client.disconnect()


def send_message(device_client: IoTHubDeviceClient, message_id: int):
    """Send a message to the IoT Hub"""
    message = json.dumps({
        "message_id": message_id,
        "deviceId": "IoT Hub Simple Python Telemetry Sender",
        "temperature": random.uniform(20, 32),
        "humidity": random.uniform(60, 80),
    })
    print(f"Sending message: {message}", flush=True)
    device_client.send_message(message)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--connection-string",
        help="Connection string for the IoT Hub",
        required=True,
    )
    parser.add_argument(
        "-i",
        "--interval-seconds",
        help="Interval in seconds between sending messages",
        default=10,
        type=int,
    )
    parser.add_argument(
        "-m",
        "--message-id",
        help="Starting message ID",
        default=1,
        type=int,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.connection_string, args.message_id, args.interval_seconds)
