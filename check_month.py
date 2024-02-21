flag = False
given_month = input("Enter a month number: ")
while flag == False:
    try:
        given_month = int(given_month)
        if 0 < given_month < 13:
            print("OK")
            flag = True
        else:
            print(f"{given_month} is not a valid month number")
            print()
            given_month = input("Enter a month number: ")
    except ValueError:
        print(f"'{given_month}' is not a valid month number")
        print()
        given_month = input("Enter a month number: ")