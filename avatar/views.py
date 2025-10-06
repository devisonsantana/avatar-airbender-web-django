from django.shortcuts import render
from django.http import HttpRequest
import requests, asyncio
from googletrans import Translator

# Create your views here.
def characters(request:HttpRequest):
    url:str = "https://last-airbender-api.fly.dev/api/v1/characters/" # Total 500 Characters ?perPage= &page=
    page:int = request.GET.get('page', 1)
    query:str = f"perPage=10&page={page}"

    response:list[dict] = requests.get(url=url, params=query).json()
    for character in response:
        afiliacao = character.get("affiliation")
        character["afiliacao_traduzida"] = asyncio.run(Translator().translate(afiliacao, 'pt', 'en')).text
        nome = character.get("name")
        character["nome_traduzido"] = asyncio.run(Translator().translate(nome, 'pt', 'en')).text
    return render(request, 'index.html', {'personagem': response, 'page': int(page)})