price = int(input("Enter the car's selling price: "))
if price < 50000:
    bonus = price * .01
else:
    bonus = price * .015
if bonus < 200:
    bonus = 200
print(f"The bonus is {bonus:.2f} euros.")