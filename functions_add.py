def add(number_one: float, number_two: float):
    # When rounding is needed, then half should be rounded up. 
    # (One trick is to add 0.5 before type conversion)
    return int(number_one + number_two + .5)

def main():
    number_one = float(input("Enter a float: "))
    number_two = float(input("Enter a float: "))
    print(f"{add(number_one, number_two)}")

main()