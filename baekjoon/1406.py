import sys


def order(words, idx, lst):
    new = words[:]
    if lst[0] == 'L':
        if idx != 0:
            idx -= 1

    elif lst[0] == 'D':
        if idx != len(words):
            idx += 1

    elif lst[0] == 'B':
        if idx == len(words):
            new = words[:idx-1]

        elif idx != 0:
            new = words[:idx-1] + words[idx:]
            idx -= 1

    elif lst[0] == 'P':
        if idx == len(words):
            new = words[:] + [lst[1]]

        else:
            new = words[:idx] + [lst[1]] + words[idx:]

        idx += 1

    return new, idx


word = list(sys.stdin.readline().strip())
idx = len(word)

m = int(sys.stdin.readline())

for i in range(m):
    lst = list(sys.stdin.readline().split())
    word, idx = order(word, idx, lst)

print(''.join(word))
