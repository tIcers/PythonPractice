# 6-1

person_1 = {'first_name': 'juan',
            'last_name': 'Escalada',
            'city': 'vancouver',
            'age': '23'}

person_2 = {'first_name': 'stefan',
            'last_name': 'Chen',
            'city': 'vancouver',
            'age': '28'}

person_list = [person_1, person_2]

full_name = person_1['first_name'] + person_1['last_name']
print(f"Full name:{full_name.title()}\nAge:{person_1['age']}\nCity:{person_1['city']}")

full_name2 = person_2['first_name'] + person_2['last_name']
print(f"Full name:{full_name2.title()}\nAge:{person_2['age']}\nCity:{person_2['city']}")

# 6-2

favorite_number = {
    'Atsuki': 7,
    'Juan': 24,
    'Stefan': '83',
    'Chis': '48',
    'Nabil': '35'
}

for name, num in favorite_number.items():
    print(f"{name}'s favorite number:{num}")

# 6-3

python_glossary = {
    'Dictionary': 'dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair.',
    'Set': 'Set has also curly bracket but it does not have key and value pair. No deplicate',
    'Tuple': 'immutable objects, which means you can not change the value in tuple',
    'List': 'mutable objects, which means you can not change the value in list',
    'Float': 'number has decimal'
}

for key, value in python_glossary.items():
    print(f"{key.title()}:{value}")

# 6-5

country_river_list = {
    'nile': 'egypt',
    'shinano': 'japan',
    'amazon': 'brazil',
}

for river, country in country_river_list.items():
    print(f"The {river.title()} runs through {country.title()}")

# 6-6

favorite_language = {
    'jen': 'python',
    'atsuki': 'python',
    'juan': 'java',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'stefan': 'php'
}

friend_list = ['chris', 'nabil', 'hoda', 'juan', 'stefan', 'edward', 'atsuki']

for name, language in favorite_language.items():
    print(f"{name.title()} loves {language.title()}")

for friend in friend_list:
    if friend in favorite_language.keys():
        print(f"{friend.title()}, thank you for taking a poll")
    else:
        print(f"{friend.title()}, please take a poll")

# 6- 7

pets = {
    'Mii': {
        'owner': 'atsuki',
        'age': '3',
        'animal': 'cat',
        'gender': 'female'
    },
    'horny': {
        'owner': 'nabil',
        'age': '10',
        'animal': 'unicorn',
        'gender': 'male'
    },
    'maru': {
        'owner': 'kosei',
        'age': '12',
        'animal': 'bird',
        'gender': 'female'
    }
}

for name, info in pets.items():
    print(f"Name:{name}is owned by {info['owner']} kind:{info['animal']} Gender:{info['gender']}")

# 6-9

favorite_places = {
    'atsuki': 'tokyo',
    'juan': 'vancouver',
    'stefan': 'Beijing'
}
for name, place in favorite_places.items():
    print(f"{name.title()}'s favorite place is {place.title()}")

# 6-11

cities = {
    'tokyo': {
        'country': 'japan',
        'population': '38 million',
        'fun fact': 'largest city in the world'
    },
    'vancouver': {
        'country': 'canada',
        'population': '675,218',
        'fun fact': ' Vancouver’s cruise ship terminal is the 4th largest in the world'
    },
    'Beijing': {
        'country': 'china',
        'population': '21.54 million',
        'fun fact': 'Beijing was not always called Beijing.'
    },

}

for city, name in cities.items():
    print(city, name['country'], name['population'], name['fun fact'])
