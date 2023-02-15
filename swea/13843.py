ip = int(input())

for case in range(1, ip+1):
    lst = list(input().split())
    stack = list()
    for i in lst:
        if i.isalnum():
            stack.append(i)
        else:
            if stack:
                a = stack.pop()
                b = stack.pop()


