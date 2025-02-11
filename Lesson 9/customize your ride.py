print ("Select your ride")
print ("1.Bike 2.Car")

choice = int(input("Enter your choice: "))

if choice == 1:
   print ("What type of bike?")
   print("1.Scooty 2.Scooter")
   choice2 = int(input("Enter your choice: "))
   if choice2 == 1:
    print("you have selected scooty")
   else:
     print("You have selected scooter")
elif choice == 2:
  print("What type of car?")
  print("1.SUV 2.Sedan")
  choice3 = int(input("Enter your choice: "))
  if choice3 == 1:
    print("You have selected Suv")
  else:
    print("you have selected Sedan")
else:
  print("WRONG CHOICE!")