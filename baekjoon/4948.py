prime = [True]*(123456*2+1)
prime[0] = False
prime[1] = False

for i in range(2, int((123456*2+1)**(1/2)+1)):
    for j in range(2, 123456):
        if i*j > 123456*2:
            break
        prime[i*j] = False

while True:
    ip = int(input())
    if ip == 0:
        break

    print(prime[ip+1:ip*2+1].count(True))
