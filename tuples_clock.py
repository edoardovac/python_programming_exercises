def roll_forward(clock_time: tuple, hours_add: int, minutes_add: int):
    new_hours = (hours_add + clock_time[0] + ((minutes_add + clock_time[1]) // 60)) % 24 
    new_minutes = (minutes_add + clock_time[1]) % 60
    return (new_hours, new_minutes)

def main():
    clock_time = (0, 0)
    print(f"The current time is {clock_time[0]:02d}:{clock_time[1]:02d}")

    given_hours = int(input("Enter hours to add: "))
    while(given_hours > -1):
        given_minutes = int(input("Enter minutes to add: "))
        clock_time = roll_forward(clock_time, given_hours, given_minutes)
        print(f"{clock_time[0]:02d}:{clock_time[1]:02d}")
        given_hours = int(input("Enter hours to add: "))
     
main()