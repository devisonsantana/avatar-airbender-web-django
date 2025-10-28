from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.cache import cache_page
from .tasks import cached_translate_g, cached_translate_d
import requests

# Create your views here.

@cache_page(60 * 60 * 24 * 30)
def characters(request: HttpRequest):
    url = 'https://last-airbender-api.fly.dev/api/v1/characters/'
    page = request.GET.get('page', 1)
    query = {'perPage': 10, 'page': page}
    data = requests.get(url, params=query).json()

    for c in data:
        nome = c.get('name', '')
        afiliacao = c.get('affiliation', '')

        c['nome_traduzido'] = cached_translate_g(nome)
        c['afiliacao_traduzida'] = cached_translate_g(afiliacao)

    return render(request, 'index.html', {'personagem': data, 'page': int(page)})
