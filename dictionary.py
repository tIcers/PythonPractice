# person

information = {"First_name": 'Atsuki', "Last_name": 'Uchida', 'City': 'Tokyo', 'Age': '24'}

print(information['First_name'])
print(information['Last_name'])
print(information['City'])
print(information['Age'])

# Favorite number

favorite_numbers = {'Jyoti': [7, 8, 3],
                    'Atsuki': [4, 99],
                    'Kosei': [2, 34],
                    'Mii': [11, 23],
                    'Hikaru': [32, 67]
                    }
for name, number in favorite_numbers.items():
    for numbers in number:
        print(f"{name}'s favorite numbers are {numbers}")

# Glossary

python_keywords = {'list': ' used to store multiple items in a single variable',
                   'dictionary': 'are used to store data values in key:value pairs',
                   'tuple': ' used to store multiple items in a single variable',
                   'int': 'integer number',
                   'float': 'decimal number',
                   'Booleans ': 'Booleans represent one of two values: True or False',
                   'set': 'Sets are used to store multiple items in a single variable',
                   'function': 'A function is a block of code which only runs when it is called.',
                   'comment': 'can be used to explain Python code.',
                   'iterator': 'is an object that contains a countable number of values.'
                   }
for (key, value) in python_keywords.items():
    print(key, value)

# rivers

rivers = {'nile': 'egypt', 'shinano': 'japan', 'amazon': 'brazil'}
for key, value in rivers.items():
    print(f"The {key} runs through {value}")
    print(f"country: {value}")
    print(f"river: {key}")

# pooling


friends = ['jack', 'tsu', 'sarah', 'edward']
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for friend in friends:
    if friend in favorite_language.keys():
        print(f"{friend}, Thank you for responding!")
    else:
        print(f"{friend}, Please take a pool!")

# people
peoples = {
    'first_info': {
        "First_name": 'Atsuki',
        "Last_name": 'Uchida',
        'City': 'Tokyo',
        'Age': '24'
    },
    'second_info': {
        "First_name": 'jyoti',
        "Last_name": 'kumari',
        'City': 'dubai',
        'Age': '27'
    },
    'third_info': {
        "First_name": 'light',
        "Last_name": 'yagami',
        'City': 'tokyo',
        'Age': '18'
    }
}

for people, user_info in peoples.items():
    full_name = user_info['First_name'] + " " + user_info["Last_name"]
    city = user_info['City']
    age = user_info['Age']

    print(f"person's name is {full_name.title()}, {age} years old, from {city.title()}")

# favorite places

favorite_places = {
    'Atsuki': 'Tokyo',
    'Lisa': 'Paris',
    'Kevin': 'NY'
}

for name, place in favorite_places.items():
    print(f"{name}'s favorite place is {place} ")

# deli & #No pastrami

sandwich_orders = ['American sub', 'Bacon', 'Beagle toast', 'BLT', 'Pastrami', 'Pastrami', 'Pastrami']
finish_sandwiches = []

print("Deli has run out of pastrami...")

while len(sandwich_orders) != 0:
    for sandwiches in sandwich_orders:
        if sandwiches == "Pastrami":
            sandwich_orders.remove(sandwiches)
        else:
            print(f"I made your {sandwiches} sandwiches")
            finish = sandwich_orders.remove(sandwiches)
            finish_sandwiches.append(finish)
print("I made all of them! ")

# Dream vacation


