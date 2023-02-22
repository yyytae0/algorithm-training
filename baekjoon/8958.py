ip = int(input())
for _ in range(ip):
    a = input()
    ans = 0
    score = 0
    for i in a:
        if i == 'O':
            score += 1
            ans += score
        else:
            score = 0
    print(ans)
