def find(n, lst, idx1, idx2):
    if n < lst[idx2]:
        idx2 = idx2 // 2
        find(n, lst, idx1, idx2)

    elif n > lst[idx]:
        idx1 = idx2

    else:
        pass



n = int(input())
lst_a = list(map(int, input().split()))
m = int(input())
lst_check = list(map(int, input().split()))
lst_a.sort()

s = ''
for i in lst_check:
    if i in lst_a:
        s = s + str(1) + '\n'

    else:
        s = s + str(0) + '\n'

print(s)
