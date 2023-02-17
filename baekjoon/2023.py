n = int(input())

prime = [1 for _ in range(10**n)]
prime[0] = 0
prime[1] = 0
for i in range(int((10**n)**(1/2))):
    if prime[i]:
        for j in range(2, (10**n)//2):
            if i*j < 10**n:
                prime[i*j] = 0

cnt = 1
lst = list()
lst.append([0])
while True:
    dummy = list()
    for i in lst[cnt-1]:
        for j in range(i*10, (i+1)*10):
            if prime[j]:
                dummy.append(j)
    lst.append(dummy)
    cnt = cnt+1
    if cnt == n+1:
        break

for i in lst[n]:
    print(i)
