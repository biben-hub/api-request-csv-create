import json
import requests
import csv
import pprint
import os.path
import tempfile
import unittest

def main():

    url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
    headers = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
#integration d'un test unitaire module écriture json
class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "wb") as f:
            f.write("Delete me!")
    
    def test_rm(self):
        #supprimer ce fichier
        rm(self.tmpfilepath)
        #tester qu'il a bien été supprimé
        self.assertFalse(os.path.isfile(self.tmpfilepath),
         "Faile to remove the file.")


#-----------------------end of test----------------------
    def read_json(): # read and saves json

        response = requests.get(url, headers=headers) #pop up for password
        # raw_data = json.loads(response.text) #dict
        with open('stop_areas_maria.json', mode="w") as file:
            json.dump(response.text, file)
# returns nothing, saves json

print(read_json())