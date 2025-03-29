# to calculate sum of whole numbers
n = int(input("Enter a number whose sum is to be calculated: "))
sum = 0
for i in range(1,n+1):
  sum = sum + i
  print("sum is", sum)