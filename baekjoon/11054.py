ip = int(input())
lst = list(map(int, input().split()))

ans_up = [1 for _ in range(ip)]
ans_down = [1 for _ in range(ip)]

for i in range(ip):
    for j in range(i):
        if lst[i] > lst[j] and ans_up[i] < ans_up[j] + 1:
            ans_up[i] = ans_up[j] + 1

for i in range(1, ip+1):
    for j in range(1, i+1):
        if lst[-i] > lst[-j] and ans_down[-i] < ans_down[-j] + 1:
            ans_down[-i] = ans_down[-j] + 1

ans = 0
for i in range(ip):
    if (ans_up[i] + ans_down[i] - 1) > ans:
        ans = ans_up[i] + ans_down[i] - 1

print(ans)
