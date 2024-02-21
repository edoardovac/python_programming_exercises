values = []
for i in range(5):
    value = int(input("Enter an integer: "))
    values.append(value)
values = sorted(values)
distint_values = set(values)
print(*distint_values, sep=", ")
print(*values, sep=", ")

