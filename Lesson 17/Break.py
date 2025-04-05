# function using break command
x = input("Enter a word: ")

for i in x:
    if i == "a":
        print("a is found")
        break
    else:
        print("a is not found")