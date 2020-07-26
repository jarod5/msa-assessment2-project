import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING: str = "HostName=msa-assessment2-project-hub.azure-devices.net;DeviceId=PythonDevice;SharedAccessKey=OJc3CyXMQZE65igOdnLBbibfrQzj0mhfgKv7crUW3Lw="

SPEED_MIN: int = 10
SPEED_MAX: int = 300

def _generate_speed() -> float:
    return random.uniform(SPEED_MIN,SPEED_MAX)

def _generate_direction(old_direction: float, speed: float) -> float:
    direction: float = old_direction + random.choice([1,-1])*speed/2
    if direction >= 360:
        direction -= 360
    if direction < 0:
        direction = 360 + direction
    return direction

def run():
    try:
        speed: float = 0.0
        direction: float = random.uniform(0,360)
        client: IoTHubDeviceClient = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        print("Sending messages, press Ctrl-c to exit")
        while True:
            speed = _generate_speed()
            direction = _generate_direction(direction,speed)
            message: str = '{"wind_speed":'+str(speed)+',"wind_direction":'+str(direction)+'}'
            print("sending: "+message)
            client.send_message(message)
            print("sent")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped")

if __name__ == "__main__":
    print("Simulated device starting up...")
    run()
