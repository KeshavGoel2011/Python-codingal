#to check prime nos. b/w a range
lower = int (input("Enter the lower number of the range: "))
upper = int (input("Enter the upper number of the range: "))
print(f"The prime no. between {lower} and {upper} are: ")

for num in range(lower,upper+1):
    if num > 1:
        for i in range (2,num):
            if num % i == 0:
                break
        else :
            print (num)