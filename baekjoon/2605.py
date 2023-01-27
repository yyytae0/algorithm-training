ip = int(input())
note = list(map(int, input().split()))
lst = list()
cnt = 1
for i in note:
    lst.insert(i, cnt)
    cnt += 1

lst.reverse()
print(*lst)
