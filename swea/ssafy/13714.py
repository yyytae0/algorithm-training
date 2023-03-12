ip = int(input())

for i in range(1, ip+1):
    a = input()
    n_a = len(a)
    b = input()
    n_b = len(b)
    dummy = 0
    for j in range(n_b-n_a+1):
        if b[j] == a[0]:
            for k in range(n_a):
                if b[j+k] == a[k]:
                    dummy = 1

                else:
                    dummy = 0
                    break
            if dummy == 1:
                print(f'#{i} 1')
                break

    if dummy == 0:
        print(f'#{i} 0')
