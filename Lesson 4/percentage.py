# calculating percentage of 5 subjects
print ("Enter marks obtained in 5 subjects")
Eng1 = int(input("Enter your English grammar marks: ")) 
Eng2 = int(input("Enter your English Literature marks: ")) 
Art = int(input("Enter your Art marks: "))
Science = int(input("Enter your Science marks: "))  
History = int(input("Enter your History marks: "))

sum = Eng1 + Eng2 + Art +Science + History
print("Sum of your marks of all the subjects : ",sum)

per = (sum/500)*100
print ("Your percentage = ",per)