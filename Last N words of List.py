string = input()
n = int(input())

words = string.split()
length_of_words = len(words) -1

modified_words = []
count = -1

for i in range(n, 0, -1):
    modified_words += [words[count]]
    count = count -1

print(modified_words)