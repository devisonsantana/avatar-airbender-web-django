from django.core.management.utils import get_random_secret_key
from . import settings
from dotenv import load_dotenv
import os

def secret_key() -> str:
    ENV_PATH = settings.BASE_DIR / 'django.env'
    key = os.getenv("DJANGO_SECRET_KEY")
    if key:
        return key
    else:
        load_dotenv(ENV_PATH)
        key = os.getenv('DJANGO_SECRET_KEY')
        if not key:
            with open(ENV_PATH, 'w') as f:
                f.write(f'DJANGO_SECRET_KEY={get_random_secret_key()}\n')
            load_dotenv(ENV_PATH)
            key = os.getenv('DJANGO_SECRET_KEY')
            return key
        else:
            return key
        
def redis(key:str='REDIS_URL') -> str:
    env = os.getenv(key=key)
    if not env:
        load_dotenv(settings.BASE_DIR / 'redis.env')
        env = os.getenv(key=key)
    return env