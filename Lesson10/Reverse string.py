 #to reverse the string
string = str(input("Enter a string: "))
string2 = ('')

for i in string:
    string2 = i + string2

print("original string is", string )
print("reversed string is", string2 )