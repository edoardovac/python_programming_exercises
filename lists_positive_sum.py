def positive_sum(integers : list):
    sum = 0
    for i in range(len(integers)):
        if integers[i] > 0:
            sum += integers[i]
    return sum

def main():
    integers = []
    for i in range(5):
        integer = int(input("Enter an integer: "))
        integers.append(integer)
    print()
    print(positive_sum(integers))

main()