try:
    number = float(input("Enter price: "))
    vat = number * .24
    final_price = number + vat
    print(f"The price with VAT is {final_price:.2f}")
except ValueError:
    print("Invalid price")