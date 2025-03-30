# Factorial with recursive function
x = int(input("Enter your number: "))

def factorial(x):
    '''This is a recursive function to find factorial of a function'''

    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
    
print (factorial.__doc__)
print("The factorial of",x,"=",factorial(x))