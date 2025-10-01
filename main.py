import requests

url:str = "https://last-airbender-api.fly.dev/api/v1/characters/" # Total 500 Characters ?perPage= &page=
query:str = f"perPage=10&page=5"

response:list[dict] = requests.get(url=url, params=query).json()