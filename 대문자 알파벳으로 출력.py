my_string = input("입력: ")

for char in my_string:
    if char.isalpha():
        print(char.upper())
    else:
        print(char)
