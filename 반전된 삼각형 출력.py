my_string = input("입력: ")
length = len(my_string)

for i in range(length, 0, -1):
    print(" " * (length - i) + my_string[0:i])

for i in range(2, length + 1):
    print(" " * (length - i) + my_string[0:i])
