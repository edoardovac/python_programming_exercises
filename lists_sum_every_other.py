def sum_every_other(values : list):
    # sum from lowest to highest value but substract the values inside values[]
    if len(values) == 0:
        return None
    else:
        others = []
        for i in range(len(values)):
            if i not in values:
                others.append(i)
        total_every_other = sum(others)
        return total_every_other

def main():
    values = []
    for i in range(4):
        given_num = int(input("Enter an integer: "))
        values.append(given_num)
    print(sum_every_other(values))

if __name__ == "__main__": 
    main()