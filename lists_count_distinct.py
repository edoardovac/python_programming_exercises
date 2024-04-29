def count_distinct(values : list):
    total_distinct = len(set(values))
    return  total_distinct

def main():
    values = ["alpha", "beta", "charlie", "charlie"]
    print(count_distinct(values))

if __name__ == "__main__": 
    main()