print("Rahim")

Productname1 = input("product name1: ")
Productprice = float(input("product price1: "))

Productname2 = input("product name2: ")
Productprice2 = float(input("product price2: "))

productname3 = input("product name3: ")
Productprice3 = float(input("product price3: "))

total = Productprice + Productprice2 + Productprice3
print(total) 

if total >= 1000 and total <= 2999:
    discount = total * 0.05
    print(discount)
      
elif total >= 3000 and total <= 4999:
    discount = total * 0.10
    print(discount) 
elif total >= 5000 and total <= 9999:
    discount = total * 0.20
    print(discount)
elif total <= 500:
    discount = total * 0.00
    print(discount)
else:
    print("Invalid")

final_price = total - discount
print(final_price)




