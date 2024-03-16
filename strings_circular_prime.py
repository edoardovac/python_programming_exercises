def main():
    pass

def is_prime(given_num : int):
    flag = True
    if 1 < given_num < 4:
        flag = True
    else:
        for i in range(2, given_num / 2):
            if given_num % i == 0:
                flag = False
    return flag        
            
def is_circular_prime(given_num : int):
    pass