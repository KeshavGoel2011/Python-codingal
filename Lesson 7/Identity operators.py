#Identity operators
x = 4

if (type(x) is int):
   print("TRUE")
else:
   print("FALSE")

x = 7.9

if (type(x) is float):
   print("TRUE")
else :
   print("FAlSE")


x = 4
y = 6
if (x is y):
   print("x and y are same")
y = 4
if (x is not y):
   print ("x and y are different")