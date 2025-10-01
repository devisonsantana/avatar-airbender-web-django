import asyncio
from googletrans import Translator
from character import Character

def to_br(text:str):
    res = asyncio.run(Translator().translate(text=text, dest="pt", src="en"))
    return res.text

def traduzir(json_data:list[dict]):
    models:list[Character] = []
    for c in json_data:
        name = c.get("name", "none").strip()
        affiliation = c.get("affiliation", "none").strip()
        character = Character(
            old_name=name,
            old_affiliation=affiliation,
            name=to_br(name),
            affiliation=to_br(affiliation)
            )
        models.append(character)
    return models