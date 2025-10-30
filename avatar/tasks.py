from django.core.cache import cache
from googletrans import Translator
from deep_translator import GoogleTranslator
import asyncio

def deep_translator(text:str, source:str='en', target:str='pt') -> str:
    if not text:
        return ''
    key = f"traducao:{source}:{target}:{text}"
    traducao = cache.get(key)
    if traducao:
        return traducao
    traducao = GoogleTranslator(source=source, target=target).translate(text)
    cache.set(key, traducao)
    return traducao

def googletrans(text:str, src:str='en', dest:str='pt') -> str:
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

def deep_translator_batch(texts:list[str], source:str='en', target:str='pt') -> list[str]:
    """Recieves a list of texts and returns a new list with translated texts"""
    if texts is None:
        return ['']
    
    texts = [t for t in texts if t]
    
    keys = [f'traducao:{source}:{target}:{t}' for t in texts]
    cached = cache.get_many(keys=keys)

    translated_texts = [v for v in cached.values()]

    uncached = [t for t, k in zip(texts, keys) if k not in cached]

    if uncached:
        traducoes = GoogleTranslator(source=source, target=target).translate_batch(uncached)
        to_cache = {
            f'traducao:{source}:{target}:{text}': translated for text, translated in zip(uncached, traducoes)
        }
        cache.set_many(to_cache)
        cached.update(to_cache)
        translated_texts += [v for v in to_cache.values()]

    return translated_texts
    
def pre_load_translate(texts:list[str], source:str='en', target:str='pt') -> None:
    """This function sets on redis all uncached texts"""
    texts = [t for t in texts if t]
    keys = [f'traducao:{source}:{target}:{text}' for text in texts]
    cached = cache.get_many(keys=keys)
    uncached = [t for t, k in zip(texts, keys) if k not in cached]
    if uncached:
        translations = GoogleTranslator(source=source, target=target).translate_batch(uncached)
        to_cache = {
            f'traducao:{source}:{target}:{text}': translated for text, translated in zip(uncached, translations)
        }
        cache.set_many(to_cache)
        cached.update(to_cache)
