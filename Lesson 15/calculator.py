#calculator function
def add(p,q):
    return p + q

def sub(p,q):
    return p - q   

def multiply(p,q):
    return p * q 

def div(p,q):
    return p / q

print ("Enter the function you want to choose")
print ("a.add")
print ("b.sub")
print ("c.multiply")
print ("d.div") 

choice = input("Enter your choice in a single letter: ")  

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == "a":
    print(num1,"+", num2,"=", add(num1,num2))
elif choice == "b":
    print(num1,"-", num2,"=", sub(num1,num2))
elif choice == "c":
    print(num1,"*", num2,"=", multiply(num1,num2))
elif choice == "d":
    print(num1,"/", num2,"=", div(num1,num2))
else:
    print("invalid input")