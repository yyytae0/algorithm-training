page = int(input())
ans_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, page + 1):
    num_str = str(i)
    for j in range(10):
        ans_lst[j] += num_str.count(str(j))

print(*ans_lst)