def mult_two(a, b):
    """
    Write a function that will receive 2 numbers as input, and it should return the multiplication of these 2 numbers.

    >>> mult_two(2,3)
    6

    >>> mult_two(1,0)
    0

    """
    return a * b


def first_word(word):
    """
    You are given a string, and you have to find its first word.
    Input: A string.
    Output: A string.
    Precondition: The text can contain a-z, A-Z and spaces.

    >>> first_word('Hello world')
    'Hello'

    """
    split_word = word.split()
    return split_word[0]


def is_accetable_password(password):
    """
    you need to create a password verification function.
    The verification condition is:
    the length should be bigger than 6.
    Input: A string.
    Output: A bool.

    >>> is_accetable_password('short')
    False

    >>> is_accetable_password('muchlonger')
    True

    """
    return len(password) > 6


def number_length(number):
    """
    You have a positive integer. Try to find out how many digits it has?
    Input: A positive Int
    Output: An Int.

    >>> number_length(10)
    2

    >>> number_length(0)
    1

    """
    word_length = len(str(number))
    return word_length


def most_frequent(data):
    """
    determines the most frequently occurring string in the sequence.
    """

    >>> most_frequent(["a", "b", "c", "a", "b", "a"])
    "a"

    >>> most_frequent(["a", "a", "bi", "bi", "bi"])
    "bi"

    return max(data, key=data.count)