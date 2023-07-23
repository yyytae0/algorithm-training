a, b = map(int, input().split())

while True:
    if a < b:
        a, b = b, a

    a, b = b, a // b

