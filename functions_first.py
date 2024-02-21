# prints the first 20 powers of two to the console

def print_powers():
    for i in range(20):
        power = 2 ** i
        print (power, end=" ")

def main():
    print_powers()

main()