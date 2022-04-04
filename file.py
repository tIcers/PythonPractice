file_name = "little_women.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()
count = 0
for line in lines:
    if "E" in line:
        count += 1

print(f"number of E's are {count}")
