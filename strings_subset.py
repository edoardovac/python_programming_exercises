first = input("Enter first string: ")
second = input("Enter second string: ")
flag = True
if len(second) == 0:
    print("Nothing to be checked")
else:
    for i in range(len(second)):
        if second[i] not in first:
            flag = False
    if flag == False:
        print("Not subset")
    else: 
        print("Subset")