import requests,flash

url_api = 'https://pokeapi.co/api/v2/pokemon/'

def informacionPokemon(nombre):
    response = requests.get(url_api + nombre)
    data = response.json()

    #Datos base 
    id = data.get('id')
    nombre_seleccionado = data.get('name')
    peso = data.get('weight')
    altura = data.get('height')
    
    data = [id,nombre_seleccionado,peso,altura]
        
    return data
    
   
        


