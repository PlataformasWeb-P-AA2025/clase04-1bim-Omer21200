import requests
import json

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    data = json.load(f)

# Lista de documentos
lista_datos = data['docs']

# Nombre de la base de datos
base_datos = "tenis002"
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Insertar uno por uno
for i, doc in enumerate(lista_datos, start=1):
    response = requests.post(url, headers=headers, json=doc)
    if response.status_code in [200, 201, 202]:
        print(f"✔ Dato {i} insertado")
    else:
        print(f"✖ Error en dato {i} | {response.status_code} | {response.text}")
