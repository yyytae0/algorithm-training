from sys import stdin, stdout


prime = [1 for _ in range(1000000)]
for i in range(2, 1001):
    if prime[i]:
        for j in range(2, 500000):
            if i * j < 1000000:
                prime[i * j] = 0

n = int(stdin.readline())
while n:
    for i in range(3, n, 2):
        if prime[i]:
            if prime[n-i]:
                stdout.write(f'{n} = {i} + {n-i}\n')
                break
    n = int(stdin.readline())
