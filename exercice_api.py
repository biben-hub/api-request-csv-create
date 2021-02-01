import json
import pprint
import requests
import csv
import logging

logging.basicConfig(filename='logFile.log', level=logging.DEBUG)
logging.info("Starting info")

#appel pour connexion à l'API +
url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization" : "88829ffa-7c9c-4051-9990-9fdf9564a298"}
response = requests.get(url, headers = headers)
data = json.loads(response.text)

print(response)
print(type(data))

areas = data["stop_areas"] #entrée dans l'API par le endpoint stop_areas (le endpoint est la clé d'entrée de communication aux data de 'lAPI)
print(type(areas))

area = areas[2]

list_ids = []

for loop_area in areas:
    if type(loop_area) == dict:
        if"id" in loop_area.keys():
            local_id = loop_area["id"]
            list_ids.append(local_id)
        else:
            print("Missing key id")
    else:
        print(f"Unexpected format {type(loop_area)}")

print(len(list_ids))

# print(type(area),area)
# print(area.keys())
print(area["id"])

list_name = []

for loop_area in areas:
    if type(loop_area) == dict:
        if "name" in loop_area.keys():
            local_name = loop_area["name"]
            list_name.append(local_name)
        else:
            print("Missing key name")
    else:
        print(f"unexpected format {type(loop_area)}")

print(area["name"])

list_timezone = []

for loop_area in areas:
    if type(loop_area) == dict:
        if "timezone" in loop_area.keys():
            local_timezone = loop_area["timezone"]
            list_timezone.append(local_timezone)
        else:
            print("Missing key name")
    else:
        print(f"Unexpected format {type(loop_area)}")

print(area["timezone"])

list_label = []

for loop_area in areas:
    if type(loop_area) == dict:
        if "label" in loop_area.keys():
            local_label = loop_area["label"]
            list_label.append(local_label)
        else:
            print("Missing key name")
    else:
        print(f"Unexeptected format {type(loop_area)}")

print(area["label"])

data = set(zip(list_ids, list_name, list_timezone, list_label))

with open("APIStropAreas.csv", "w") as file:
    head = ["ids", "name", "time", "label"]
    fileWriter = csv.writer(file, delimiter = ";" )
    fileWriter.writerow(i for i in head)

    for row in data:
        fileWriter.writerow(row)

#soit on fait beautify soit on créer l'architecture de l'api dynamiquement