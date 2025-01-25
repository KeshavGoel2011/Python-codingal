# Count the notes required
Amount = int(input("Enter the amount for withdrawal: "))

note_1 = Amount // 100
note_2 = (Amount % 100)//50
note_3 = ((Amount%100)%50)//10

print ("100$ notes required : ", note_1)
print ("50$ notes required : ", note_2)
print ("10$ notes required : ", note_3)