file_name = "little_women.txt"

with open(file_name) as file_object:
    lines = file_object.read()
count = 0
for line in lines:
    if "A" in line:
        count += 1

print(f"number of A are {count}")
