dct = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

ip = int(input())
for i in range(1, ip+1):
    a = input()
    ans = ''
    for j in a:
        ans = dct[j] + ans

    print(f'#{i} {ans}')
