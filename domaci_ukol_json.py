import requests
import json

ICO=input("Zadej IČO subjektu:")
response = requests.get('https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/'+ ICO)
data = response.json()
print(data["obchodniJmeno"])
print(data["sidlo"]["textovaAdresa"])