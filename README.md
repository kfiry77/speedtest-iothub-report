# speedtest-iothub-report
A telemetry report of internet connection speed to Azure iot hub

## Installation

### 1. Azure deployment

1. create Azure iot hub 
2. create Device id on Azure iot hub
3. create shared access key to the device. 
4. get device connection string. 

### 2. Device Application

1. speedtest cli tool as it described (here)[https://www.speedtest.net/apps/cli] 
1. clone this repository
1. create ``config.json`` in application folder
1. modify config.json:
```json
{
  "connection_string": "HostName=IOT_HUB_NAME.azure-devices.net;DeviceId=_DEVICE_ID;SharedAccessKey=DEVICE_SAS",
  "logfile": "./Log/speedtest.log"
}
```

5. use the command ```crontab -e``` and sdd the following line to crontab for lines for periodic telemetrics 
```shell
# speedtest telemetry
*/30 * * * * python3 /path/to/repo main.py & 

```

### references:

- https://www.speedtest.net/apps/cli

### TODO:
[v] Send the telemetry to cosmos-db
[] create a script that build the azure deployment. 
[] Add git hook for a automatic updates on the device. 


