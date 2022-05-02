# the number of words

def count_words(file_name):
    try:
        with open(file_name) as file:
            file = file.read()
    except FileNotFoundError:
        print(f"I am sorry, {file_name} does not exist. ")
    else:
        word = file.split()
        count_word = len(word)
        print(f"{file_name} has around {count_word} words")


file_names = ['alice.txt', 'siddhartha.txt', 'moby.txt', 'little_women.txt']
for file_name in file_names:
    count_words(file_name)

# error handling
print('enter the number, type q if you want to stop the program')
while True:
    try:
        prompt1 = input("enter the number: ")
        if prompt1 == 'q':
            break
        prompt1 = int(prompt1)
        prompt2 = input("enter the number: ")
        if prompt2 == 'q':
            break
        prompt2 = int(prompt2)
    except ValueError:
        print("Input is not a number! ")
    else:
        result = prompt1 + prompt2
        print(result)

