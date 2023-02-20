n = int(input())
ans = 0
stack = list()
now = 0
for i in range(n):
    hw = input()
    if hw != '0':
        a, b, c = map(int, hw.split())
        if now:
            stack.append(now)
        now = [b, c-1]
        if not now[1]:
            ans += now[0]
            if stack:
                now = stack.pop()
            else:
                now = 0
    else:
        if now:
            now[1] -= 1
            if not now[1]:
                ans += now[0]
                if stack:
                    now = stack.pop()
                else:
                    now = 0

print(ans)