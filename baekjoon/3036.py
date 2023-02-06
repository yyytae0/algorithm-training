import math

n = int(input())
lst = list(map(int, input().split()))

for i in range(1, n):
    dummy = math.gcd(lst[0], lst[i])
    print(f'{lst[0]//dummy}/{lst[i]//dummy}')
