# restrant

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")


queen = Restaurant('the mean queen', 'pizza')
print(queen.name)
print(queen.cuisine_type)

queen.describe_restaurant()
queen.open_restaurant()

sushiro = Restaurant('sushiro', 'sushi')
print(sushiro.name)
print(sushiro.cuisine_type)

sushiro.describe_restaurant()
sushiro.open_restaurant()

jyojyoen = Restaurant('jyojyoen', 'yakiniku')
print(jyojyoen.name)
print(jyojyoen.cuisine_type)

jyojyoen.describe_restaurant()
jyojyoen.open_restaurant()


# user

class User():
    def __init__(self, first_name, last_name, user_id, address):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.address = address

    def describe_user(self):
        print(f"User first name: {self.first_name}\n")
        print(f"User last name: {self.last_name}\n")
        print(f"User Id: {self.user_id}\n")
        print(f"User address: {self.address}\n")

    def greeting(self):
        print(f"Good morning, {self.first_name}")


first_user = User('atsuki', 'uchida', '12345', 'japan')
first_user.greeting()
first_user.describe_user()

second_user = User('Mii', 'chan', '67890', 'tokyo')
second_user.greeting()
second_user.describe_user()
