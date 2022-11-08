import requests
import json


r = requests.get('https://akabab.github.io/superhero-api/api/all.json')
list_heroes = json.loads(r.text)
list_of_compared_heroes = ['Hulk', 'Captain America', 'Thanos']
heroes_and_their_intelligence_stats = {}
for hero in list_of_compared_heroes:
    for hero_dict in list_heroes:
        for key, value in hero_dict.items():
            if value == hero:
                heroes_and_their_intelligence_stats.update({hero_dict["name"]: hero_dict["powerstats"]["intelligence"]})

max_intelligence = max(heroes_and_their_intelligence_stats.values())
for hero_name, intelligence in heroes_and_their_intelligence_stats.items():
    if intelligence == max_intelligence:
        print(f'{hero_name} has the most intelligence stat: {intelligence}')



