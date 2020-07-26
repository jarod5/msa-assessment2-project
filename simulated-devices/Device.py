import time
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING: str = "HostName=msa-assessment2-project-hub.azure-devices.net;DeviceId=PythonDevice;SharedAccessKey=OJc3CyXMQZE65igOdnLBbibfrQzj0mhfgKv7crUW3Lw="

def run():
    try:
        client: IoTHubDeviceClient = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        print("Sending messages, press Ctrl-c to exit")
        while True:
            message: str = '{"test":1.0}'
            print("sending...")
            client.send_message(message)
            print("sent")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped")

if __name__ == "__main__":
    print("Simulated device starting up...")
    run()
