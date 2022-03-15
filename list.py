import os

# list
list_of_names = ['juan', 'stefan', 'nabil', 'chris']
greeting = f"Hello {list_of_names[0].title()}\nHello {list_of_names[1].title()}\nHello {list_of_names[2].title()}\nHello {list_of_names[3].title()}\n"
print(greeting)

list_of_cars = ['Honda', 'Nissan', 'Toyota']
print(f"I would like to use {list_of_cars[0]}'s car")

# guest list
guest_list = ['yoshiki', 'tetsuya', 'yuta']
invite_message1 = f"Hi, {guest_list[0].title()}! You are invited to dinner"
invite_message2 = f"Hi, {guest_list[1].title()}! You are invited to dinner"
invite_message3 = f"Hi, {guest_list[2].title()}! You are invited to dinner"
print(invite_message1, invite_message2, invite_message3, sep=os.linesep)
print(f"{guest_list[-1]} can not make the dinner")
guest_list[-1] = 'taichi'
print(guest_list)
print("It seems we found big table")
guest_list.insert(0, 'haruki')
guest_list.insert(2, 'moe')
guest_list.insert(4, 'hikaru')
print(guest_list)

print("wow, we only have two spaces! ")
changed_guest = guest_list.pop(-1)
print(f"I am sorry, {changed_guest}. We can not invite you for dinner")
changed_guest = guest_list.pop(-2)
print(f"I am sorry, {changed_guest}. We can not invite you for dinner")
changed_guest = guest_list.pop(-3)
print(f"I am sorry, {changed_guest}. We can not invite you for dinner")
changed_guest = guest_list.pop(0)
print(f"I am sorry, {changed_guest}. We can not invite you for dinner")

print(f"{guest_list[0]}\tand {guest_list[1]} are still invited")
del guest_list[0]
del guest_list[0]
print(guest_list)

# sort vs sorted
# "sort" is sorting something permanently but "sorted" is temporary

five_cities = ['Tokyo', 'Paris', 'New York', 'Vancouver', 'London']
print(five_cities)

five_cities.sort()
print(five_cities)

print(sorted(five_cities))

five_cities.reverse()
print(five_cities)

five_cities.reverse()
print(five_cities)

five_cities.sort()
print(five_cities)

five_cities.sort(reverse=True)
print(five_cities)


# dinner guest

print(len(guest_list))