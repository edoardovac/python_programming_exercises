given_length = int(input("How many surnames? "))
surnames = []
for i in range(given_length):
    surname = input("Enter a surname: ")
    surnames.append(surname.strip().capitalize())
surnames = sorted(set(surnames))
print()
print(*surnames)