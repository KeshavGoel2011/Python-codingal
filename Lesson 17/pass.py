#pass function
for x in range (20):
    if x % 20 == 0 :
        print ("Divisible by 20")
    elif x % 15 == 0 :
        pass
    elif x % 5 == 0:
        print ("Divisible by 5") 
    elif x % 3 == 0 :
        print ("Divisible by 3")
    else:
        print (x)