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
    print(f"{key}:{value}")