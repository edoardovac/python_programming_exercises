from urllib.request import urlopen
url = "https://www.mit.edu/~ecprice/wordlist.10000"
word_list = urlopen(url).read().splitlines()

counters = [0] * 23
for i in range(len(word_list)):
    index = len(word_list[i])
    counters[index] = word_list[i]

print(word_list)