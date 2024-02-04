'''
Crear una funció que mostri, per consola, i guardi en un arxiu extern, 
un JSON amb una key de nom book que contindrà titel, cover, year i pages. 
Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values). 
'''
import json
def makeJSON():
    llibres = []
    for i in range(4):
        llibres.append(
            {    
                "books": {
                    
                    "title":f"El llibre {i+1}",
                    "cover":f"cover llibre {i+1}",
                    "year":f"{i+1*1981}",
                    "pages":f"{i+1*250}"
                }
            }
        )        

    # crear
    with open('llibres.json', 'w') as file:
        json.dump(llibres, file, indent=2)

makeJSON()