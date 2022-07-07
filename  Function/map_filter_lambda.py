def square(num):
    return num ** 2


my_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(square, my_num)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "Even"
    else:
        return mystring[0]


names = ['Andy', 'Eva', 'Atsuki']

print(list(map(splicer, names)))


def check_num(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_num, my_nums)))

# better to use lambda when you only want to use one time but never use the function again

lambda num: num ** 2

print(square(5))

print(list(map(lambda num: num ** 2, my_nums)))

"""Use map() to create a function which finds the length of each word in the phrase (broken by spaces) and returns the values in a list.

The function will have an input of a string, and output a list of integers."""


def word_length(phrase):
    return list(map(lambda x: len(x), phrase.split()))


word_length('How long are the words in this phrase')
