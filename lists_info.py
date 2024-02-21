integers = []
for i in range(5):
    given_int = int(input("Enter an integer: "))
    integers.append(given_int)
print()
print(f"count: {len(integers)}")
print(f"min: {min(integers)}")
print(f"max: {max(integers)}")
print(f"sum: {sum(integers)}")