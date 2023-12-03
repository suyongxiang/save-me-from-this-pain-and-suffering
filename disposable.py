
discountentry = 9/10
discountshoe = 2/4
price = 0
soccer = input("u want soccer? yes or no")
amount = float(input("amount of balls"))
if soccer == "yes":
    price = 5*amount
entry = input("u want entry? yes or no")
amounts = float(input("amount of students"))
amountd = float(input("amount of NON students"))
if entry == "yes":
    price = price + 10*discountentry*amounts + 10*amountd   
shoe = input("u want shoe? yes or no")
amount = float(input("amount of shoes"))
amounts = float(input("amount of students"))
amountd = float(input("amount of NON students"))
if shoe == "yes":
    price = price + 6*discountshoe*amounts + 6*amountd
print ("price is", round(price,2))