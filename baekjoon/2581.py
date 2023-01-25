M = int(input())
N = int(input())

prime = [True]*(N+1)
prime[0] = False
prime[1] = False

for i in range(2, int(N**(1/2))+1):
    for j in range(2, int(N/2)+1):
        if i*j > N:
            break

        prime[i*j] = False

total = 0
for i in range(M, N+1):
    if prime[i]:
        if total == 0:
            min_prime = i
        total = total + i

if total == 0:
    print(-1)

else:
    print(total)
    print(min_prime)
