from pprint import pprint

import requests


class Hero:

    def __init__(self, url: str):
        self.url = url

    def status(self):
        response = requests.get(self.url)
        return response.json()['results'][0]['powerstats']['intelligence']


Hulk = Hero('https://superheroapi.com/api/2619421814940190/search/Hulk')
pprint(f'Интеллект Халка - {Hulk.status()}')
Captain_America = Hero('https://superheroapi.com/api/2619421814940190/search/Captain_America')
pprint(f'Интеллект Капитана Америки - {Captain_America.status()}')
Thanos = Hero('https://superheroapi.com/api/2619421814940190/search/Captain_America')
pprint(f'Интеллект Таноса - {Thanos.status()}')
print(f'Самый(е) умный(е) герой(и) имеет(ют) Интеллект - \
{max(Hulk.status(), Captain_America.status(), Thanos.status())} и его(их) имя(имена) см. выше')
