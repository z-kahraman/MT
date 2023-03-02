import requests
import json
from configparser import ConfigParser


# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

# Get values
serverInfo = config_object["SERVERINFO"]
url = serverInfo["url"]
headers = serverInfo["headers"]
data = serverInfo["data"]
robotName = serverInfo["robotName"]


# Burada str object has no attribute items hatası var düzeltilecek
response = requests.post(url, json=data, headers=headers, verify=False)


print("###############################\n")
print("Json Response: ")
print(response.json())

print("\n###############################")
jsonResponse = response.json()
dataSize = len(jsonResponse["data"])
print(f"Json Data Size: {dataSize}")

control = ""

if dataSize == 0:
    print("Data veya robot tanımlı değildir..")
else:
    for i in range(0,dataSize):
        # Robot name == Robot_xxxx
        if jsonResponse["data"][i]["name"] == robotName:
            control = "OK"
            print(f"Bulunulan satır sayısı = {i}")

            print("\n###################################")

            controlStatus = jsonResponse["data"][i]["status"] 
            print(controlStatus)

            if controlStatus != None:
                if "AVAILABLE" in controlStatus:
                    print("Robot available")
                else:
                    print(f"Robot {controlStatus}")
            else:
                print("Status Unknown")

            print("###################################")
            print(jsonResponse["data"][i])
            break
        else:
            control = "NOK"
            continue

    print("###################################")
    if control == "OK":
        print("Robot bulundu")
    else:
        print("Robot bulunamadiii")




