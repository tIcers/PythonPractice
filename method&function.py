"""LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5"""


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        result = min(a, b)
        return result
    else:
        return max(a, b)


"""ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False"""


def animal_crackers(word):
    splited_word = word.split()
    return splited_word[0][0] == splited_word[1][0]


def makes_twenty(n1, n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20


"""OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'"""


def old_macdonald(name):
    first_half = name[:3]
    rest = name[3:]

    return first_half.capitalize() + rest.capitalize()


"""MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'"""


def master_yoda(text):
    word_list = text.split()
    reverssed = word_list[::-1]
    ss = " ".join(reverssed)
    return ss


"""ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True"""


def almost_there(n):
    if n > 90 and n < 110:
        return True
    elif n > 190 and n < 210:
        return True
    else:
        return False
