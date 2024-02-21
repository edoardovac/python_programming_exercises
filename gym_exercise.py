visits = int(input("Enter the number of days of gym visits per year: "))
day_pass = float(input("Enter price for a day pass: "))
yearly_fee = float(input("Enter yearly membership fee: "))
difference = (visits * day_pass) - yearly_fee
print()
if difference > 0:
    print(f"Paying the yearly membership fee is {difference:.2f} euros cheaper")
elif difference == 0:
    print("There is no price difference")
elif difference < 0:
    difference = abs(difference)
    print(f"Buying day passes is {difference:.2f} euros cheaper")