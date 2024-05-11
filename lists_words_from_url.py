from urllib.request import urlopen
url = "https://www.mit.edu/~ecprice/wordlist.10000"
word_list = urlopen(url).read().splitlines()
counters = [0] * 23
sum = 0

for word in word_list:
    length = len(word)
    counters[length] += 1

word_count = len(word_list)
sum = 0
for word in word_list:
    sum += len(word)
word_average = sum / word_count

print(f"{word_count} words")
print(f"The average word length is {word_average}")
print("Length Count")
for i in range(1, 23):
    print(f"{i:6d} {counters[i]:5d}")