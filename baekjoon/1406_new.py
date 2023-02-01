from sys import stdin


def order(com):
    global left
    global right
    global idx
    if com[0] == 'L':
        if len(left) != 0:
            right[-idx] = left.pop()
            idx += 1

    elif com[0] == 'D':
        if idx != 1:
            left.append(right[-idx + 1])
            right[-idx + 1] = ''
            idx -= 1

    elif com[0] == 'B':
        if len(left) != 0:
            left.pop()

    elif com[0] == 'P':
        left.append(com[1])


idx = 1
left = list(stdin.readline())
left.pop()
right = [''] * 500000
ip = int(input())
for i in range(ip):
    command = list(stdin.readline().split())
    order(command)

print(''.join(left+right))
