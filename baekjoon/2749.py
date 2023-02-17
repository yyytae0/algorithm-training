n = int(input())

mod = 10**6
p = 15*(10**5)
d1 = 0
d2 = 1
for i in range(2, (n%p)+1):
    d1, d2 = d2, (d1 + d2) % 1000000
print(d2 % 1000000)
