from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.cache import cache_page
from .tasks import deep_translator, deep_translator_batch
import requests

# Create your views here.

# cache page for 1 hour
@cache_page(60 * 60 * 1)
def characters(request: HttpRequest):
    url = 'https://last-airbender-api.fly.dev/api/v1/characters/'
    TOTAL_CHARS = 497
    page = request.GET.get('page', 1)
    per_page = 12
    query = {'perPage': per_page, 'page': page}
    total_pages = TOTAL_CHARS / per_page

    data = requests.get(url, params=query).json()

    for c in data:
        nome = c.get('name', '')
        afiliacao = c.get('affiliation', '')
        aliados = c.get('allies')
        inimigos = c.get('enemies')

        c['nome'] = deep_translator(nome)
        c['afiliacao'] = deep_translator(afiliacao)
        c['aliados'] = deep_translator_batch(aliados)
        c['inimigos'] = deep_translator_batch(inimigos)

    return render(request, 'index.html', {'personagem': data, 'page': int(page), 'total_pages': total_pages})
