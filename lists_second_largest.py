def second_largest(values : list):
    if len(values) in [0, 1]:
        return None
    else:
        values_set = list(set(values))
        highest = max(values_set)
        values_set.remove(highest)
        second_largest = max(values_set)
        return second_largest

def main():
    values = [1, 2, 3, 4]
    return second_largest(values)

if __name__ == "__main__": 
    main()