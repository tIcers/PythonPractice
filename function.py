# message

def display_message():
    print("I am learning function in python!")


display_message()


# favorite book

def favorite_book(title):
    print(f"My favorite book is {title.title()}")


favorite_book("Death note")


# T-Shirt
def make_shirt(size, text):
    print(f"Your shirt size is {size}, printed {text}")


make_shirt("L", "Python is fun ")
make_shirt(size="L", text="Python is fun ")


# Python T
def python_T(size, message):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')


python_T('large', 'I love Python!')
python_T(message="Readability counts.", size='medium')


# City

def describe_city(city, country="Japan"):
    print(f"{city} is in {country}")


describe_city("Tokyo")
describe_city("Osaka")
describe_city("Vancouver", country="Canada")

# City Names

# 8-6
