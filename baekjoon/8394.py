n = int(input())
d = [1, 0]
for i in range(2, n+1):
    d[0], d[1] = (d[0]+d[1]) % 10, d[0] % 10
print(sum(d) % 10)
