import math

ip = int(input())

for i in range(ip):
    lst = list(map(int, input().split()))
    ans = math.factorial(lst[1])/(math.factorial(lst[1]-lst[0])*math.factorial(lst[0]))
    print("%d" % ans)
