from django.shortcuts import render
from django.http import HttpResponse
import requests
import asyncio
from googletrans import Translator

# Create your views here.
def characters(request):
    url:str = "https://last-airbender-api.fly.dev/api/v1/characters/" # Total 500 Characters ?perPage= &page=
    query:str = f"perPage=5&page=1"

    response:list[dict] = requests.get(url=url, params=query).json()
    for character in response:
        afiliacao = character.get("affiliation", "none")
        character["afiliação_traduzida"] = asyncio.run(Translator().translate(afiliacao, 'pt', 'en')).text
        nome = character.get("name", "none")
        character["nome_traduzido"] = asyncio.run(Translator().translate(nome, 'pt', 'en')).text
    return render(request, 'index.html', {'response':response})