ip = int(input())

for case in range(ip):
    a, b = map(int, input().split())
    while a != b:
        if a > b:
            a = a//2
        else:
            b = b//2
    print(10*a)
