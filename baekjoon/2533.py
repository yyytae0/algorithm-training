n = int(input())
lst = [{} for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    lst[a][b] = 1