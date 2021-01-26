import json
import pprint
import requests
import csv

'''
# f = open('stop_areas.json', "r")

# data = json.load(f)
# for i in data['emp_details']:
#     print(i)

# f.close()
'''
'''
with open('stop_areas.json', "r") as read_file:
    data = json.load(read_file)
    json.dumps(data, sort_keys=True, indent=4)

pp = pprint.PrettyPrinter(indent=4, width=80, compact=False)
pp.pprint(data)
'''
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