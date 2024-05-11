def sum_every_other(values : list):
    if len(values) == 0:
        return None
    else:
        return sum(values[::2])


def main():
    values = [1, 2, 3, 4, 5]
    print(sum_every_other(values))

if __name__ == "__main__": 
    main()