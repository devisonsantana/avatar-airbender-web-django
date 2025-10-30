from django.core.management.base import BaseCommand
from avatar.tasks import pre_load_translate
import requests

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--pages', type=int, default=50,
            help='Número total de páginas a pré-traduzir (padrão: 50).'
        )
        parser.add_argument(
            '--per-page', type=int, default=10,
            help='Quantidade por página conforme API (padrão: 10).'
        )
        parser.add_argument(
            '--src', type=str, default='en', help='Idioma origem (padrão: en).'
        )
        parser.add_argument(
            '--dest', type=str, default='pt', help='Idioma destino (padrão: pt).'
        )

    def handle(self, *args, **options):
        pages = options['pages']
        per_page = options['per_page']
        src = options['src']
        dest = options['dest']
        api_url = "https://last-airbender-api.fly.dev/api/v1/characters/"

        self.stdout.write(self.style.NOTICE(f"Starting pre-translate of {pages} pages (per_page={per_page})"))

        for page in range(1, pages + 1):
            self.stdout.write(f"Processing page {page}/{pages}...")

            data = requests.get(url=api_url, params={'perPage': per_page, 'page': page}).json()
            
            nomes = [item.get('name', '') for item in data]
            afiliacoes = [item.get('affiliation', '') for item in data]
            aliados = [i for item in data for i in item.get('allies', '')]
            inimigos = [i for item in data for i in item.get('enemies', '')]

            pre_load_translate(nomes + afiliacoes + aliados + inimigos, source=src, target=dest)

            if not any(nomes or afiliacoes or aliados or inimigos):
                self.stdout.write(self.style.WARNING("Empty page, ending the task."))
                break