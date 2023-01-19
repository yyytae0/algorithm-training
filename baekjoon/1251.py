ip = list(input())

word = ip[:-2]
word.reverse()

print(word)

words = list()
for i in range(len(word)):
    words.append(''.join(word[i:]))

words.sort()
print(len(words[0]))
