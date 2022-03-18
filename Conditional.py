# alien color

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points")
elif alien_color == 'yellow':
    print("You just earned 10 points")
elif alien_color == 'red':
    print("You just earned 15 points")
else:
    print("ok")

# user
user = 'Atsuki'
usernames = ['admin', 'eric', 'atsuki', 'hikaru', 'rei']

if user == 'admin':
    print(f'Hello {user}, would you like to see a status report? ')

else:
    print(f"Hello {user}")

# no user

user_name_list = []

if len(user_name_list) == 0:
    print('We need to find some users!')

# checking usernames

current_users = ['Atsuki', 'Hikaru', 'Rei', 'Juan', 'Stefan']
new_users = ['Atsuki', 'Dago', 'Chris', 'Michel', 'Andy']

for cu in current_users:
    if cu in new_users:
        print(f'{cu} You need a new user name')
    else:
        print(f"User name {cu} is available!")

# Ordinal num

numbers_list = [num for num in range(1, 10)]
for number in numbers_list:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}rd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")