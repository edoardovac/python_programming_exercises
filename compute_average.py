from statistics import mean
given_number = float(input("Enter first number: "))
if given_number == 0:
    print("Nothing to be calculated")
else:
    numbers = []
    while given_number != 0:
        numbers.append(given_number)
        given_number = float(input("Enter next number: "))
    average = mean(numbers)
    print(f"The average is {average:.2f}")