import requests
import json

Nazev_subjektu=input("Zadej nazev subjektu subjektu:")
response = requests.post('https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat',headers={
    "accept": "application/json",
    "Content-Type": "application/json",
},data='{"obchodniJmeno": "'+ Nazev_subjektu +'"}')
data = response.json()
print(data["pocetCelkem"])
for item in data["ekonomickeSubjekty"]:
    print(item["obchodniJmeno"])
    

