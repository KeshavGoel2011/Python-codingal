#To check whether a number is >or< 15:

a = int(input("Enter the number to be checked: "))

if a > 15:
    print(a, "is greater than 15")
    print("I am in If block")

else:
    print(a, "is smaller than 15")
    print("I am in Else block")

print("I am not in If or Else block")