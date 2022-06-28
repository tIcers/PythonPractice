import string


def greet_user(username):
    print(f"Hello, {username.title()}!")


greet_user('atsuki')


# in this case, atsuki is an example of argument whereas username is a parameter

def favorite_book(titile):
    print(f"One of my favorite book is {titile.title()}")


favorite_book('death note')


# positional argument is the same order of parameters
# keyword arguments where each argument consist of valuable name nad a value; and lists and dictionaries of values.


def describe_pet(pet_name, animal_type='cat'):
    print(f"I have a {animal_type.title()}")
    print(f"The name is {pet_name.title()}")


# if you do not provide the specific thing, that will be ok since it is going to be considered as default

# but it seems python will consider it as a positional argument so need to be careful
describe_pet('mii')


# T-shirt
# positional

# keyword
def make_shirt(message='I love python', size='L'):
    if size == 's':
        print(f"you ordered {size}size of t thirts")
        print("Hum i do not like C and Java")
    print(f"you have {size} size of t shirt")

    print(f"Message:{message}")


make_shirt()
make_shirt(size='s')


def describe_city(city, country='japan'):
    print(f"{city} is in {country}")


describe_city('yokohama')
describe_city('osaka')
describe_city('vancouver', country='canada')


def city_country(city, country):
    return f"{city.title()},{country.title()}"


print(city_country('tokyo', 'japan'))
print(city_country('van', 'canada'))
print(city_country('ny', 'usa'))


def make_album(name, album_title, song=None):
    album_list = {
        'album name': name,
        'title': album_title,
    }
    if song:
        album_list['song'] = song
    return album_list


print(make_album('atsu', 'tokai', 'hoo'))


def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)


def palindrome(word):
    return word == word[::-1]


print(palindrome('nurses run'))
print(palindrome('abcba'))
print(palindrome('helleh'))
print(palindrome('eunice'))

all_alpha = list(string.ascii_lowercase + string.ascii_uppercase)


def ispangram(word):
    for words in word:
        if all_alpha not in words:
            return False
        else:
            return True


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("i love you eunice"))


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


2


def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]


def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'


def master_yoda(text):
    return ' '.join(text.split()[::-1])
