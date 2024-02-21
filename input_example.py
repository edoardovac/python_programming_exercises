name = input("Your name: ")
# age = input("Your age: ")
# age += 1 crashes the program
# need to convert input to integer
age =int(input("Your age: "))
age += 1
# this way it works
print(name)
print(age)