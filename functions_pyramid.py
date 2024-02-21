def print_pyramid(height):
    # you need as many lines as the given height, meaning that height + 1 is needed inside range()
    # for i in range(start is 1, end is height + 1, step is 1 because you cannot skip lines)
    
    # * position is inversely proportional to height, meaning that in line 1 the * is in the 4th spot
    # meaning that you have 3 spaces, meaning that the number of spaces is height - i 
    # in line 1 you then have 4 (height) - 1 (i) = 3
    # in line 2 you have 4 - 2 = 2 and so on

    # * grows by 2 per each line (1, then 3, then 5 and so on...)
    # i is 1, 2, 3, 4
    # * = i + 1 doesn't work because you'd get ** in the first line
    # * = 2i doesn't work because you'd get ** in the first line
    # * = 2i - 1 works because you'd get * in the first line, then *** in the second
    for i in range(1, height + 1):
        print(f"{(height - i) * ' '}{(2 * i - 1) * '*'}")

def main():
    height = int(input("Enter pyramid height: "))
    print_pyramid(height)

main()