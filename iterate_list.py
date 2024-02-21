names = ["kari", "juhani", "sanna"]

for x in names:
    print(x)
#    print(x + " ", end="")
    
print(names, sep=", ")
print(*names, sep=", ")
print(*names, sep=" - ")