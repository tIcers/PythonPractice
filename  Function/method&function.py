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
    if 90 < n < 110:
        return True
    elif 190 < n < 210:
        return True
    else:
        return False


"""FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False"""


def has_33(nums):
    for num in range(0, len(nums) - 1):
        if nums[num] == 3 and nums[num + 1] == 3:
            return True
    return False


"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'"""


def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result


"""BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If 
their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) 
exceeds 21, return 'BUST' blackjack(5,6,7) --> 18 blackjack(9,9,9) --> 'BUST' blackjack(9,9,11) --> 19 """


def blackjack(*nums):
    result = sum(nums)
    if result <= 21:
        return result
    elif result > 21 and 11 in nums:
        result -= 10
        return result
    else:
        return 'BUST'


"""SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14"""


def summer_69(nums):
    result = 0
    add = True
    for num in nums:
        while add:
            if num != 6:
                result += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return result


"""SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False"""


def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


"""LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5"""


def second_lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)

    else:
        return max(a, b)


print(second_lesser_of_two_evens(2, 5))
print(second_lesser_of_two_evens(2, 4))

"""ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False"""


def second_animal_crackers(word):
    splited_word = word.split()
    if splited_word[0][0] == splited_word[1][0]:
        return True
    else:
        return False


print(second_animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

"""OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'"""


def second_old_macdonald(word):
    first = word[:3]
    second = word[3:]
    return first.capitalize() + second.capitalize()


print(second_old_macdonald('macdonald'))  # slicing is good

"""MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'"""


def second_master_yoda(sentence):
    return sentence.split()[::-1].


print(second_master_yoda('I am home'))
