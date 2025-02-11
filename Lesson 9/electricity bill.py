#check the electricity bill
units = int(input("Enter the  no. of units you consumed: "))

if units < 50:
    amt = units* 2.60
    surcharge = 25
elif units <= 100 :
    amt = 130 + ((units - 50)*3.25)
    surcharge = 35
elif units <= 200:
    amt = 130 + 162.50 + ((units - 100)*5.25)
    surcharge = 45
else :
    amt = 130 + 162.50 + 526 + ((units - 200)*8.45)
    surcharge = 75

total = amt + surcharge
print(f"Your total bill is {total}")

