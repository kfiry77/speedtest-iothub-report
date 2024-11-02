# speedtest-iothub-report
A telemetry report of internet connection speed to Azure iot hub

## Installation

### 1. Azure deployment

1. create Azure iot hub 
2. create Device id on Azure iot hub
3. create shared access key to the device. 
4. get device connection string. 

### 2. Device Application

1. install speedtest cli tool as it described [here](https://www.speedtest.net/apps/cli)
1. clone this repository and enter the create directory
   ```sh
   git clone https://github.com/kfiry77/speedtest-iothub-report.git
   cd speedtest-iothub-report
   ``` 
1. create virtual environment and install python packages. 
   ```sh
   python3 -m venv ./venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   ```
1. create ``config.json`` in application folder with the following format: 
   ```json
   {
    "connection_string": "HostName=IOT_HUB_NAME.azure-devices.net;DeviceId=_DEVICE_ID;SharedAccessKey=DEVICE_SAS",
    "logfile": "./Log/speedtest.log"
   }
   ```
1. use the command ```crontab -e``` and sdd the following line to crontab for lines for periodic telemetrics 
   ```sh
   # speedtest telemetry
   */30 * * * * (/bin/bash -c "cd /path/to/repo && source venv/bin/activate && python3 main.py  >> /path/to/logfile.log 2>&1 &")
   ```
### references:

- https://www.speedtest.net/apps/cli

### TODO:

- [x] Send the telemetry to cosmos-db
- [x] Build a Azure web app, to present the result with table. 
- [ ] Build a Azure app to show the result with Graph
- [ ] create a script that build the azure deployment. 
- [ ] Add git hook for a automatic updates on the device. 


