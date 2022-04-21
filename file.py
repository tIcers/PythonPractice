def main():
    file_name = "little_women.txt"

    with open(file_name) as file_object:
        content = file_object.read()
    count = 0
    for line in content:
        if "A" in line:
            count += 1

    print(f"number of A's is {count}")


if __name__ == "__main__":
    main()
