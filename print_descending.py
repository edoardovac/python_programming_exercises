try:
    given_number = int(input("Enter an integer: "))
    if given_number > 0:
        sum = 0
        for given_number in range(given_number, 0, -1):
            sum += given_number
            print(given_number, end=" ")
        print()
        print(f"The sum is {sum}")
    else:
        print("Nothing to be printed")
except ValueError:
    print("Nothing to be printed")