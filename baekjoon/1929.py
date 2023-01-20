ip = list(map(int, input().split()))

prime = [True]*(ip[1]+1)
prime[0] = False
prime[1] = False

for i in range(2, int(ip[1]**(1/2))+1):
    for j in range(2, int(ip[1]/2)+1):
        if i*j > ip[1]:
            break

        prime[i*j] = False

for i in range(ip[0], ip[1]+1):
    if prime[i]:
        print(i)
