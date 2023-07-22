my_string = input("입력: ")

for i in range(len(my_string)):
    print("*" * (i+1) + my_string[i:])
