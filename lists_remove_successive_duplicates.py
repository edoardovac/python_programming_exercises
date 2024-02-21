# doesn't work, need to be fixed

def remove_successive_duplicates(values : list):
    if len(values) in [0, 1]:
        return None
    else:    
        singles = [values[0]]
        for i in range(len(values)):
            if values(i) in singles and i != 0:
                # would this break everything ? 
                values.remove(i)
        return values

def main():
    values = [3, 1, 1, 2, 1, 2, 2, 2, 3]
    values = remove_successive_duplicates(values)
    print(*values)
    

if __name__ == "__main__": 
    main()