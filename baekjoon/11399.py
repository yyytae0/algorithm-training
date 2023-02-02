ip = int(input())
lst = list(map(int, input().split()))
lst.sort()

for i in range(1, ip):
    lst[i] = lst[i] + lst[i-1]

print(sum(lst))
