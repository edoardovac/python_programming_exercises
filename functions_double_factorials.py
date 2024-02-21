def double_factorial(given_number : int):
    total = 1
    if given_number in [0, 1]:
        return total
    else:
        if given_number % 2 == 0: #quindi pari
                for i in range(2, given_number + 1, 2):
                    total *= i
                return total
        else:
            for i in range(1, given_number + 1, 2):
                total *= i
            return total

def main():
    for i in range(0, 10):
        print(f"{i}!! = {double_factorial(i)}")

main()
