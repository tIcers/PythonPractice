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

import random
import time
import math


def calculateMouseSpeed(first, second, ms):
    coordinateList = []
    for x in range(11):
        x1 = random.randint(1, 1280)
        y1 = random.randint(1, 800)
        ms = time.time()

        x2 = random.randint(1, 1280)
        y2 = random.randint(1, 800)
        me = time.time()

        first = (x2 - x1)
        second = (y2 - y1)

        distance = math.sqrt((first ** 2) + (second ** 2))
        distance_time = me - ms
        speed = distance / distance_time
        coordinateList.append(speed)
        time.sleep(0.1)
    return coordinateList


"""Use filter to return the words from a list of words which start with a target letter."""


def filter_words(word_list, letter):
    return list(filter(lambda x: x[0] == 'h', word_list))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')


import random
import time
import math

coordinatesList = []
duration = []

for x in range(10):
    ms = time.time()
    x1 = random.randrange(0, 1280)
    y1 = random.randrange(0, 800)
    first = (x1, y1)
    time.sleep(1)

    x2 = random.randrange(0, 1280)
    y2 = random.randrange(0, 800)
    second = (x2, y2)
    me = time.time()

    duration.append(me - ms)
    coordinatesList.append((first, second))

print(coordinatesList)
def calculateMouseSpeed(coordinatesList, duration):
    total_distance = 0
    total_duration = 0
    for x in range(10):
        distance = math.sqrt((coordinatesList[x][0][0] - coordinatesList[x][1][0]) ** 2 + (coordinatesList[x][0][1] - coordinatesList[x][1][1]) ** 2)
        total_distance += distance
        total_duration += duration[x]

    return total_distance/total_duration

print(calculateMouseSpeed(coordinatesList,duration))


