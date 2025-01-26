#to check profit
Cost_Price = float(input("Enter the Cost price of the product: "))
Selling_Price = float(input("Enter the Selling price of the product: "))

if Cost_Price<Selling_Price :
    Profit = Selling_Price - Cost_Price
    print("Your profit is : ", Profit)

else:
    print("No profit")
