def print_rectangle():
    height = int(input("Enter height: "))
    width = int(input("Enter width: "))
    for i in range(height):
        for j in range(width):
            print("*", end="")
        print()

def main():
    print_rectangle()

main()