ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = list()
    for i in range(5):
        ans.append(lst[-i-1])
        ans.append(lst[i])
    print(f'#{case}', *ans)
