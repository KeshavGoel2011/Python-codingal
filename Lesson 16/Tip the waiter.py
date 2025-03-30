#tip the waiter
bill_amount = float(input("please enter the bill amount= " ))
tip_perc = float(input("please enter the tip percent= " ))

def t_cal(bill_amount,tip_perc):
    total = bill_amount*(1+0.01*tip_perc)
    total = round(total,2)
    print("You have to pay",total)

t_cal(bill_amount,tip_perc)