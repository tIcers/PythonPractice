# 9-1
from random import randint
from random import choices

class Restaurant:
    def __init__(self, name, food_type):
        self.name = name
        self.food_type = food_type
        self.number_served = 0

    def describe_restaurant(self):
        message = f"{self.name} has {self.food_type} type of food"
        print(message)

    def show_restaurant(self):
        message = f"{self.name} is now opened. Check it out"
        print(message)

    def hours(self):
        message = f"{self.name} is opened from 8 am to 9 pm "
        message += f"{self.food_type} is limited per day"
        print(message)

    def served_num(self, number_served):
        self.number_served = number_served
        print(self.number_served)

    def updated_served_num(self, additional_served):
        self.number_served += additional_served
        print(self.number_served)


class IceCreamStand(Restaurant):

    def __init__(self, name, food_type='ice cream'):
        super.__init__(name, food_type)
        self.tastes = []

    def show_all_tastes(self):
        for taste in self.tastes:
            print(f"They are all tastes:{taste}")


restaurant = Restaurant("Otoya", 'Japanese food')
print(restaurant.name)
print(restaurant.food_type)

restaurant.describe_restaurant()
restaurant.show_restaurant()
restaurant.hours()

restaurant.served_num(2)
restaurant.updated_served_num(3)

ice = IceCreamStand('New ice cream')
ice.tastes = ['vanila', 'choco', 'wasabi']
ice.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.user_id = user_id
        self.attemp = 0

    def describe_user(self):
        message = f"Full name: {self.first_name + self.last_name}\n Age:{self.age}"
        print(message)

    def greet_user(self):
        message = f"Welcome to the page, {self.first_name}"

    def increment_login_attempts(self):
        self.attemp += 1
        print(self.attemp)

    def reset_login_attempts(self):
        self.attemp = 0
        print(self.attemp)


class Admin(User):
    def __init__(self, first_name, last_name, age, user_id):
        super.__init__(first_name, last_name, age, user_id)
        self.privileges = []

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"You can do {privilege}")


atsuki = User('Atsuki', 'Uchida', 23, 123456)
stefan = User('stefan', 'chen', 28, 2239874567)

atsuki.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
atsuki = Admin('Atsuki', 'Uchida', 23, 123456)
atsuki.show_privileges()

atsuki.describe_user()
atsuki.greet_user()
atsuki.increment_login_attempts()
atsuki.increment_login_attempts()
atsuki.reset_login_attempts()

stefan.describe_user()
stefan.greet_user()


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


dice_6 = Die(sides=10)

result = []

for dice in range(10):
    result = dice_6.roll_die()
    result.append(result)
print(result)

lottary = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']


print(f"{choices(lottary,k=5)} are win the prize! ")
