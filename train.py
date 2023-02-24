left = []
start = int(input())
for i in range(10):
    n = int(input())
    if n < start:
        for i in left:
            if n > i:
                pass
        else:
            left.append(n)