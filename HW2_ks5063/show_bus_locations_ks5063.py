from __future__ import print_function
import sys

import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python  show_bus_locations_ks5063.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

print("Bus Line : " + sys.argv[2])
if not data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0].get('VehicleActivity'):
    print('Number of Active Buses : 0')
else:
    print("Number of Active Buses : " + str(len(data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])))

i=0
  
for row1 in data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"]:
    if row1.get('VehicleActivity'):
        for row2 in row1["VehicleActivity"]:
            print("Bus " + str(i) + " is at latitude " + str(row2["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]) + " and longitude " + str(row2["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]))
            i+=1