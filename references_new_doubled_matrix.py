from copy import deepcopy

def new_doubled_matrix(matrix: list):
    copy = deepcopy(matrix)
    for row in copy:
        for i in range(len(row)):
            row[i] *= 2
    return copy

def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = new_doubled_matrix(m1)
    print(m1)
    print(m2)

main()