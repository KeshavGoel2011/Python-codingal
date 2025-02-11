#To check whether a student is allowed to take the exam later
med_cause = input("Do you have any medical cauuse? (Y/N): ")
atten = int(input("Please enter your attendance: "))

if med_cause == "Y":
    print("You are eligible for the exam")
else:
    if atten >= 75 :
        print ("You are eligible for the exam")
    else:
        print("You are not eligible for the exam")