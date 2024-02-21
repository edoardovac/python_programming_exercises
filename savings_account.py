interest_rate = float(input("Enter interest rate: "))
tax_rate = float(input("Enter capital income tax rate: "))
deposit = float(input("Enter initial deposit: "))
years = int(input("Enter number of years: "))
year = 0

tax_rate_perc = 1 - (tax_rate / 100)
interest_perc = interest_rate / 100

print()
for years in range(years):
    year += 1
    interest = deposit * interest_perc
    profit = interest * tax_rate_perc
    deposit += profit
    print(f"Year {year}: {deposit:.2f}")