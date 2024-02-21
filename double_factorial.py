given_number = int(input("Enter a non-negative integer: "))
total = 1
if given_number < 0:
    print("Please enter a non-negative integer")
elif given_number in [0, 1]:
    print(f"{given_number}!! = {total}")
else:
    if given_number % 2 == 0: #quindi pari
        for i in range(2, given_number + 1, 2):
            total *= i
    else:
        for i in range(1, given_number + 1, 2):
            total *= i
    print(f"{given_number}!! = {total}")