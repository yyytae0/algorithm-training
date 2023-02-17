def check(n):
    for i in range(3, int(n**(1/2)+1), 2):
        if not n%i:
            return False
    return True


n = int(input())

# prime = [1 for _ in range(10**n)]
# prime[0] = 0
# prime[1] = 0
# for i in range(int((10**n)**(1/2))):
#     if prime[i]:
#         for j in range(2, (10**n)//2):
#             if i*j < 10**n:
#                 prime[i*j] = 0

cnt = 2

lst = [2, 3, 5, 7]
while cnt < n+1:
    dummy = list()
    for i in lst:
        for j in range(i*10 + 1, (i+1)*10, 2):
            if check(j):
                dummy.append(j)
    lst = dummy[:]
    cnt = cnt+1
    if cnt == n+1:
        break

for i in lst:
    print(i)
