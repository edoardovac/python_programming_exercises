given_weekday_num = input("Enter a weekday number: ")
try:
    given_weekday_num = int(given_weekday_num)
    if 0 < given_weekday_num < 8:
        print("OK")
    else:
        print("Please enter an integer between 1 and 7")
except ValueError:
    print("Please enter an integer between 1 and 7")