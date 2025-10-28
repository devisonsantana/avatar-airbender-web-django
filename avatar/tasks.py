from django.core.cache import cache
from googletrans import Translator
from deep_translator import GoogleTranslator
import asyncio

def cached_translate_d(text, src='en', dest='pt') -> str:
    if not text:
        return ''
    key = f"traducao:{src}:{dest}:{text}"
    traducao = cache.get(key)
    if traducao:
        return traducao
    traducao = GoogleTranslator(source=src, target=dest).translate(text)
    cache.set(key, traducao)
    return traducao

def cached_translate_g(text, src='en', dest='pt') -> str:
    if not text:
        return ''
    key = f"traducao:{src}:{dest}:{text}"
    traducao = cache.get(key)
    if traducao:
        return traducao
    translator = Translator()
    traducao = asyncio.run(translator.translate(text=text, src=src, dest=dest)).text
    cache.set(key, traducao)
    return traducao

def pre_load_translate(texts, src='en', dest='pt'):
    keys = [f"traducao:{src}:{dest}:{text}" for text in texts]
    cached = cache.get_many(keys=keys)
    uncached = [t for t, k in zip(texts, keys) if k not in cached]
    if uncached:
        translations = GoogleTranslator(source=src, target=dest).translate_batch(uncached)
        to_cache = {
            f"traducao:{src}:{dest}:{text}": translated for text, translated in zip(uncached, translations)
        }
        cache.set_many(to_cache)
        cached.update(to_cache)
