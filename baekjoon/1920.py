from sys import stdout


n = int(input())
lst_a = list(map(int, input().split()))
m = int(input())
lst_check = list(map(int, input().split()))
lst_a.sort()
check = dict()
for i in lst_a:
    check[i] = 1

for i in lst_check:
    try:
        stdout.write(str(check[i]) + '\n')

    except KeyError:
        stdout.write('0\n')
