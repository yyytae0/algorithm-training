ip = int(input())

for _ in range(ip):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    rule = list(list(map(int, input().split())) for _ in range(k))
    target = int(input())
