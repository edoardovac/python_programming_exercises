def pow_2_3(given_int: int):
    # pow is built-in method for exponential pow(int, esponente)
    return (pow(given_int, 2), pow(given_int, 3))

def main(): 
    x = int(input("Enter an integer: ")) 
    p2, p3 = pow_2_3(x) 
    print(p2) 
    print(p3) 

if __name__ == "__main__": 
    main()