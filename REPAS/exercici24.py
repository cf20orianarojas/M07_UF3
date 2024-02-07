# Crear una funció que llegeixi el JSON de l’exercici anterior i surti el resultat (en format json) per consola.
import json
def readJSON():
    with open('llibres.json', 'r') as file:
        result = json.load(file)
        print(json.dumps(result, indent=2))
readJSON()