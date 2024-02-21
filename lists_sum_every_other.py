def sum_every_other(values : list):
    # sum from lowest to highest value but substract the values inside values[]
    if len(values) == 0:
        return None
    else:
        lowest = min(values)
        highest = max(values)
        total = highest - lowest
        total_every_other = total - sum(values)
        return total_every_other
    
def main():
    pass

if __name__ == "__main__": 
    main()