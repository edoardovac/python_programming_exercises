def common_members(first_list : list, second_list : list):
    for member in first_list:
        if member in second_list:
            return True
    return False
    
def main():
    first_list = [1, 2, 3]
    second_list = [3, 5, 6]
    print(common_members(first_list, second_list))

if __name__ == "__main__":
    main()