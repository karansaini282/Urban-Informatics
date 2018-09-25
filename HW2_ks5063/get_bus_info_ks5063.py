from __future__ import print_function
import sys

import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python  get_bus_info_ks5063.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

fout = open(sys.argv[3], "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")


for row1 in data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"]:
    if row1.get('VehicleActivity'):
        for row2 in row1["VehicleActivity"]:
            if(row2["MonitoredVehicleJourney"]["OnwardCalls"].get("OnwardCall")):
                for row3 in row2["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"]:
                    fout.write(str(row2["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"])+","+str(row2["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])+","+str(row3["StopPointName"])+","+str(row3["Extensions"]["Distances"]["PresentableDistance"])+"\n")
            else:
                fout.write(str(row2["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"])+","+str(row2["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])+","+"N/A"+","+"N/A"+"\n")
                
fout.close()