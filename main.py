import requests
import asyncio
from googletrans import Translator

url:str = "https://last-airbender-api.fly.dev/api/v1/characters/" # Total 500 Characters ?perPage= &page=
query:str = f"perPage=20&page=1"

response:list[dict] = requests.get(url=url, params=query).json()

def translate_characters(json_data:list[dict]):
    models:list[dict] = []
    for c in json_data:
        name = asyncio.run(Translator().translate(text=c.get("name", "none").strip(), dest="pt", src="en")).text
        affiliation = asyncio.run(Translator().translate(text=c.get("affiliation", "none affiliation").strip(), dest="pt", src="en")).text
        character = {
            "nome": name,
            "afiliação": affiliation
        }
        models.append(character)
    return models

characters = translate_characters(response)
for c in characters:
    print(f"Nome: {c.get("nome")}")
    print(f"Afiliação: {c.get("afiliação")}")
    print(f"{'-' * 30}")