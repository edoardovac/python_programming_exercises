def second_largest(values : list):
    if len(values) in [0, 1]:
        return None
    else:
        highest = max(values)
        second_largest = values[0]
        for i in range(len(values)):
            if second_largest < values[i] < highest:
                second_largest = values[i]
        return second_largest

def main():
    values = []
    for i in range(4):
        value = int(input("Enter a number: "))
        values.append(value)
    print(second_largest(values))

if __name__ == "__main__": 
    main()