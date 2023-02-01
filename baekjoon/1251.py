ip = list(input())

anslst = list()
word = ip[:-2]
word.reverse()
words = list()
for i in range(len(word)):
    words.append(''.join(word[i:]))

words.sort()
first = words[:]

for i in first:
    word = ip[len(i):-1]
    word.reverse()
    words = list()
    for j in range(len(word)):
        words.append(''.join(word[j:]))

    words.sort()
    second = words[:]

    for j in second:
        third = ip[(len(i)+len(j)):]
        third.reverse()
        third = ''.join(third)
        ans = i+j+third
        anslst.append(ans)

anslst.sort()
print(anslst[0])
