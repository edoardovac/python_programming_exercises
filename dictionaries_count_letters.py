from urllib.request import urlopen

url = "https://www.mit.edu/~ecprice/wordlist.10000"
content = urlopen(url).read().decode("UTF-8")

letters_count = {}

for letter in content:
    lower =  letter.lower()
    if lower.isalpha():
        if lower in letters_count:
            letters_count[lower] += 1
        else:
            letters_count[lower] = 1

for letter, count in sorted(letters_count.items()):
    print(f"{letter}: {count}")