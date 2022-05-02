# pizza

list_of_pizza = ['Cheese Pizza', 'Pepperoni Pizza', 'Margherita Pizza']

for pizza in list_of_pizza:
    print(f"I like {pizza}")

print("I really like pizza!")

# Animal

animals = ['Cat', 'Dog', 'Parakeets']
for animal in animals:
    print(f"{animal} would make a great pet")
print("But I love cat")

# counting to twenty

for number in range(21):
    print(number)

# to one million
# numbers = []
# for number in range(1_000_001):
#     numbers.append(number)
numbers = list(range(1, 1_000_001))
print(sum(numbers))
print(min(numbers))
print(max(numbers))

odd_num = []
for odd in range(1, 21, 2):
    odd_num.append(odd)

odd_num = list(range(1, 21, 2))
print(odd_num)

# Three
three_list = []
for three in range(3, 30):
    value = three * 3
    three_list.append(value)
print(three_list)

# list comprehension
three_list = [three * 3 for three in range(3, 30)]
print(three_list)

# cubes
cubes = []
for cube in range(1, 11):
    new_value = cube ** 3
    cubes.append(new_value)
print(cubes)

# list comprehension
cubes = [cube ** 3 for cube in range(1, 11)]
print(cubes)

# slice
print(list_of_pizza[:3])

print(list_of_pizza[1:])

print(list_of_pizza[-3:])


list_of_pizza.append('Chicago pizza')

friend_pizzas = list_of_pizza[:]
friend_pizzas.append('california Pizza')

print(f"My favorite pizzas are {list_of_pizza}")
print(f"My friend's favorite pizzas are {friend_pizzas}")

for my_pizza in list_of_pizza:
    print(f"My favorite pizzas are {my_pizza}")

for pizzas in friend_pizzas:
    print(f"My friend's favorite pizzas are {pizzas}")

# more loops


