from datetime import date
from calendar import monthrange

def print_month_calendar(year : int, month : int):
    month_names = ["", 
                   "January", 
                   "February", 
                   "March", 
                   "April", 
                   "May",
                   "June",
                   "July", 
                   "August", 
                   "September", 
                   "October", 
                   "November", 
                   "December"]
    # create date obj
    my_date = date(year, month, 1)
    # determine number of days in a month
    days_in_the_month = monthrange(my_date.year, my_date.month)[1]
    # determine day of the week (1 = Monday)
    day_of_week = my_date.weekday() + 1
    # the easiest way to print a day number is as below
    # print(f"{day:4d}")

    # separate for loop that prints the first line of day numbers only
    # second for loop to print the other lines of day numbers

    # there is one leading space on each calendar line
    # all day numbers can be printed with the same format specifier
    print(f" > {month_names[month]} {year} <")
    print(f" Mon Tue Wed Thu Fri Sat Sun")

    #day_of_week ==> 1 is first day --> you can get the weekday
    # first week
    """
    count = 0
    day_num = my_date.day
    for i in range (8):
        if i == day_of_week:
            day = day_num + count
            print(f"{day:4d}", end="")
            day_of_week += 1
            count += 1
        else:
            # not the ideal way
            print(f"   ", end="")  
    # second week
    # check what number is the first monday --> you know that already
    # meaning that you need a loop from that day until the end of the month
    # then to know when to go to the next line day
    # if i % 7 == day_of_week % 7
    for i in range (day_of_week, days_in_the_month):
        day = day_num + count
        if (i % 7) == ((day_of_week) % 7):
            print()
            print(f"{day:4d}", end="")
        else:
            print(f"{i:4d}", end="")
        count += 1
    """
    day_week = []
    count = 1
    for i in range (8):
        if i == day_of_week:
            day_week.append(count)
            count += 1
        else:
            day_week[i].append("   ")
    print(*day_week)

     

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print_month_calendar(year, month)

main()