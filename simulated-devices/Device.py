import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING: str = "HostName=msa-assessment2-project-hub.azure-devices.net;DeviceId=PythonDevice;SharedAccessKey=OJc3CyXMQZE65igOdnLBbibfrQzj0mhfgKv7crUW3Lw="

SPEED_MIN: int = 10
SPEED_MAX: int = 300

def _generate_speed() -> float:
    """ Returns a random number between min and max speed to use as the new wind speed """
    return random.uniform(SPEED_MIN,SPEED_MAX)

def _generate_direction(old_direction: float, speed: float) -> float:
    """ Uses the previous wind direction and current wind speed to calculate and return a new wind direction """
    #randomly chooses whether to go clockwise or counter-clockwise and adds half the speed to the previous direction
    #(this is making the assumption that more energetic winds change more violently)
    direction: float = old_direction + random.choice([1,-1])*speed/2
    #if 360 or over, then fix it so it remains within a range of 0 to 360
    if direction >= 360:
        direction -= 360
    #if under 0, then fix it so it remains within the range of 0 to 360
    if direction < 0:
        direction = 360 + direction
    return direction

def run():
    try:
        speed: float = 0.0
        #initialises direction to a random number since _generate_direction needs something to start with
        direction: float = random.uniform(0,360)
        #establish connection
        client: IoTHubDeviceClient = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        print("Sending messages, press Ctrl-c to exit")
        while True:
            #update wind speed and direction
            speed = _generate_speed()
            direction = _generate_direction(direction,speed)
            #create and send message
            message: str = '{"wind_speed":'+str(speed)+',"wind_direction":'+str(direction)+'}'
            print("sending: "+message)
            client.send_message(message) #message is actually sent here
            print("sent")
            time.sleep(1)
    except KeyboardInterrupt:
        #when Ctrl-c is pressed allow the function to finish so the program can stop running
        print("Stopped")

if __name__ == "__main__":
    print("Simulated device starting up...")
    run()
