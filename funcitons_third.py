def compute_discount(price, discount_percentage):
    discount = price * discount_percentage / 100
    return discount

def main():
    price = float(input("Enter price: "))
    discount_percentage = float(input("Enter discount percentage: "))
    discount = compute_discount(price, discount_percentage)
    print(f"The discount is {discount:.2f} euros")

main()