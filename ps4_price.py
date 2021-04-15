saved_amount = int(input('Please enter your saved amount: '))
ps4_price = 100

if ps4_price/2 >= saved_amount:
    print("You must save more, keep saving!")
elif saved_amount >= ps4_price:
    print("Yippee! You can buy your PS4")
elif ps4_price/2 < saved_amount:
    print("You saved more than half, keep saving!")