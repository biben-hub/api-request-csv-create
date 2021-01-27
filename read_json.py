import json
import pprint
import csv


'''
Méthode 1

f = open('stop_areas.json', "r")

data = json.load(f)
for i in data['emp_details']:
    print(i)

f.close()
'''

# Méthode 2
with open('stop_areas.json', "r") as read_file:
    data = json.load(read_file)
    json.dumps(data, sort_keys=True, indent=4)

pp = pprint.PrettyPrinter(indent=4, width=80, compact=False)
pp.pprint(data)
