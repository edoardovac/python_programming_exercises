def transpose_dictionary(vocabulary: dict):
    new = vocabulary.copy()
    vocabulary.clear()
    for key, value in new.items():
        vocabulary[value] = key
    return vocabulary

def main():
    vocabulary = {"cat": "kissa", "dog": "koira", "bird": "lintu"}
    print(vocabulary)
    transpose_dictionary(vocabulary)
    print(vocabulary)
main()