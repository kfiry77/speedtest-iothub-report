import uuid
from azure.iot.device import IoTHubDeviceClient, Message
import subprocess
import json

def send_telemetry(con_string, telemetry):
    device_client = IoTHubDeviceClient.create_from_connection_string(con_string)
    msg = Message("ISP Connection Speed")
    msg.message_id = uuid.uuid4()
    msg.content_encoding = "utf-8"
    msg.content_type = "application/json"
    msg.custom_properties["conn_down_speed"] = telemetry.download_speed
    msg.custom_properties["conn_up_speed"] = telemetry.upload_speed
    msg.custom_properties["ping_latency"] = telemetry.ping_latency
    device_client.send_message(msg)
    device_client.shutdown()

class Telemetry:
    def __init__(self):
        pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('config.json') as f:
        dic = json.load(f)
    con_string = dic['connection_string']
    result = subprocess.run(['speedtest', '--format', 'json'], capture_output=True)

    line = result.stdout.decode().strip()

    with open(dic['logfile'], "a") as file_object:
        file_object.write(line)
        file_object.write('\n')

    output = json.loads(line)
    telemetry = Telemetry()
    telemetry.download_speed = int(output['download']['bandwidth']) / (1024 * 1024) * 8
    telemetry.upload_speed = int(output['upload']['bandwidth']) / (1024 * 1024) * 8
    telemetry.ping_latency = float(output['ping']['latency'])
    send_telemetry(con_string, telemetry)
    print(f"Download speed: {telemetry.download_speed} Mbps")
    print(f"Upload speed: {telemetry.upload_speed} Mbps")
    print(f"Ping Latency: {telemetry.ping_latency} mSec")
