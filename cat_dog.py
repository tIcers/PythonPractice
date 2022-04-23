def file_finder(file_name):
    try:
        with open(file_name) as file:
            file = file.read()

    except FileNotFoundError:
        # print(f"{file_name} does not exist, I am sorry. ")
        pass
        # silently
    else:
        print(f"{file}\n")


file_lists = ['cat.txt', 'dog.txt', 'bird.txt']
for file_list in file_lists:

    file_finder(file_list)