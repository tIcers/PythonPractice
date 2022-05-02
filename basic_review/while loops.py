# 7-1

prompt = input('What kind of car are you looking for?: ')
print(f"Let me find {prompt}")

# 7-2

number_of_ppl = input("How many people do you have for dinner?: ")
if int(number_of_ppl) > 8:
    print("Sorry, you have to wait for table a bit")
else:
    print("table is ready!")

# 7-3

prompt = input("Enter the number: ")

number_checker = int(prompt) % 10
if number_checker == 0:
    print("It is a multiple of 10")

else:
    print("Probably not")

# 7-4

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break
# 7-5

prompt = "What is your age?: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("You can get a free ticket")

    elif age < 13:
        print("$10")
    else:
        print("$15")

# 7-8

sandwich_orders = ['Normal Chicken Sandwich', 'Fish Sandwich', 'Fried Egg Sandwich', 'Grilled Cheese Sandwich']
finished_sandwiches = []

while sandwich_orders:
    finished = sandwich_orders.pop()
    print(f"I made {finished}")
    finished_sandwiches.append(finished)

print(finished_sandwiches)

#7-10
dream_list = {}
name_prompt = "What is your name?: "
place_prompt = "If you could visit one place in the world, where would you go?: "
question_prompt = "Would you continue to asking? Y/N: "

while True:
    name = input(name_prompt)
    place = input(place_prompt)
    dream_list[name] = place
    repeat = input(question_prompt)
    if repeat != 'y':
        break


print("---This is the list of places---")

for key, value in dream_list.items():
            print(f"{key}:{value}")

