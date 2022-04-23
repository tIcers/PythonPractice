# with open("learning_python.txt") as file:
#     content = file.read().replace('python', 'c')
#     print(content)
#
# with open("learning_python.txt") as file:
#     for lines in file:
#         lines.replace('python', 'c')
#         print(lines.strip())
#
# with open("learning_python.txt") as file:
#     lines = file.readlines().replace('python', 'c')
#     for line in lines:
#         print(line.strip())

with open('guest.txt', 'w') as file:
    file.write("Hikaru\n")
    file.write("Atsuki\n")
    file.write("Juan\n")
    file.write("Stefan\n")

filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book.")

file_name = 'programming.txt'

print("Enter 'quit' when you are finished.")

while True:
    poll = input("What is the reason you love programming?: ")
    if poll =='quit':
        break
    else:
        with open(file_name,'a') as file:
            file.write(f"{poll}\n")
        print("Thank you for answering")
