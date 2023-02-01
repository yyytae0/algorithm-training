import sys


def order(idx, lst):
    global words
    if lst[0] == 'L':
        if idx != 0:
            while words[idx-1] == 0:
                idx -= 1
                if idx == 1:
                    break
            idx -= 1

    elif lst[0] == 'D':
        if idx != len(words):
            while words[idx] == 0:
                idx += 1
            idx += 1

    elif lst[0] == 'B':
        if idx == len(words):
            words.pop()
            idx -= 1

        elif idx != 0:
            words[idx-1] = 0
            idx -= 1

    elif lst[0] == 'P':
        if idx == len(words):
            words.append(lst[1])

        elif words[idx] == 0:
            words[idx] = lst[1]

        elif words[idx-1] == 0:
            words[idx-1] = lst[1]

        else:
            words = words[:idx] + [lst[1]] + words[idx:]

        idx += 1

    return idx


words = list(sys.stdin.readline().strip())
idx = len(words)

m = int(sys.stdin.readline())

for i in range(m):
    lst = list(sys.stdin.readline().split())
    idx = order(idx, lst)

ans = ''
for i in words:
    if i == 0:
        continue

    else:
        ans = ans + i

print(ans)
