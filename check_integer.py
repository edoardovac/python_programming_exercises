given_number = input("Enter an integer: ")
try:
    given_number = int(given_number)
    print("OK")
except ValueError:
    print(f"'{given_number}' is not an integer")