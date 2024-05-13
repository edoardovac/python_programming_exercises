given_ints = []

for i in range(7):
    given_int = int(input("Enter an integer: "))
    given_ints.append(given_int)

for i in range(0, len(given_ints) - 1, 2):
    given_ints[i], given_ints[i + 1] = given_ints[i + 1], given_ints[i]

print(given_ints)