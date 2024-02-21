def compute_earnings(hourly_wage, hours_worked):
    if hours_worked > 40:
        normal = hourly_wage * 40
        overtime = hourly_wage * (hours_worked - 40) * 1.5
        return normal + overtime
    else:
        return hourly_wage * hours_worked

def main():
    hourly_wage = float(input("Enter wage: "))
    hours_worked = int(input("Enter hours: "))
    print(f"The earnings are {compute_earnings(hourly_wage, hours_worked):.2f}")

main()