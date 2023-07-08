# to check if the credit score is good and then ask for down payment

price_of_house = 10000

has_good_credit = True

if has_good_credit:
    print(f"You need to pay 10% as downpayment")
    print(f"Your final payment will be {price_of_house*0.1}")
else:
    print(f"You need to pay 20% as downpayment")
    print(f"Your final payment will be {price_of_house*0.2}")


