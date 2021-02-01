import json
import requests

# d'abord on stock l'url avec son endpoint et ses authorization qu'on prend chez le fournissuer de l' API
url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization" : "88829ffa-7c9c-4051-9990-9fdf9564a298"}

#on se crée une fonction qui va nous appeler l'api
#récupérer les data de l'api et les ecrire dans un json
#nous dire que la connexion est ok en nous renvoyant un message
def connex_rw_data_json_api():
    response = requests.get(url, headers = headers)
    with open('stop_areas_file.json', mode="w") as file:
            json.dump(response.text, file)
    
    print(response, "\n Le fichier à bien été crée")


connex_rw_data_json_api()

#fonction pour lire les données de mon json
def read_links():
    
    with open('stop_areas_file.json') as fichier_areas:
        data = json.load(fichier_areas)

        links = data["links"]
        list_hrefs = []
        print(type(data))
        print(data)
    
#     links = data['links']
#     #list_hrefs = []
    
#     print(type(links))

# read_links()

read_links()