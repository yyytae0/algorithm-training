ip = int(input())
lst = list(map(int, input().split()))

for i in range(1, ip):
    lst[i] = max(lst[i], lst[i] + lst[i - 1])

print(max(lst))
