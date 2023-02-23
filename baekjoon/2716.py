ip = int(input())

for case in range(ip):
    s = input()
    stack = list()
    n = 0
    cnt = 0
    mx = 0
    for i in s:
        if i == '[':
            stack.append(i)
            n += 1

        else:
            stack.pop()
            cnt += 1
            if cnt > mx:
                mx = cnt
            n -= 1
            if n == 1:
                cnt = 1

    print(2**mx)
