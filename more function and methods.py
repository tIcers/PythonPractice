"""Write a function that computes the volume of a sphere given its radius."""


def vol(rad):
    return (4 / 3) * 3.14 * rad ** 3


"""Write a function that checks whether a number is in a given range (inclusive of high and low)"""


def ran_bool(num, low, high):
    return num in range(low, high + 1)


"""Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
HINT: Two string methods that might prove useful: .isupper() and .islower()

"""


def up_low(s):
    upper_count = 0
    lower_count = 0
    for ss in s:
        if ss.isupper():
            upper_count += 1
        elif ss.islower():
            lower_count += 1
        else:
            continue;
    print(s)
    print(f"Number of Upper case characters : {upper_count}")
    print(f"Number of Lower case characters : {lower_count}")


"""Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]"""


def unique_list(lst):
    return list(set(lst))


"""Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24"""


def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


"""Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, 
or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing 
with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing 
notation. """


def palindrome(s):
    reveresed_text = s[::-1]
    return s[0] == s[-1]


"""write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"""
import string


def ispangram(str1):
    alphabet_list = list(string.ascii_lowercase + string.ascii_uppercase)
    for al in str1:
        if al not in alphabet_list:
            return False
        else:
            return True
