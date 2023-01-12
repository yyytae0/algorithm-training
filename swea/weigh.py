
def cnt_weight(lst, right, left, cnt):
    n = len(lst)
    new_lst = lst
    new_right = right
    new_left = left
    if n == 1:
        cnt += 1

    else:
        for i in range(n):
            new_right.append(lst[i])
            new_lst.pop(i)
            print(n)
            if sum(new_right) > sum(new_left):
                print(new_lst)
                new_left.append(lst[i])
                cnt_weight(new_lst, right, new_left, cnt)
                break

            else:
                print(new_right)
                cnt_weight(new_lst, new_right, new_left, cnt)


    return cnt



"""

ip = int(input())

for i in range(ip):
    n = int(input())
    right = list()
    left = list()
    lst = list(map(int, input().split()))
    ans = cnt_weight(lst, right, left)
    print(ans)
"""

lst = [1, 2, 3]
right = []
left = []
a = cnt_weight(lst, right, left, 0)
print(a)
