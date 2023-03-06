from collections import deque


def bfs():
    q = deque()
    q.extend([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]])
    cnt = 9
    while q:
        v = q.popleft()
        for i in range(v[0]+1, 10):
            q.append([i, int(str(i)+str(v[1]))])
            ans.append(int(str(i)+str(v[1])))
            cnt += 1


n = int(input())
ans = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if n > 1022:
    print(-1)
else:
    bfs()
    ans.sort()
    print(ans[n])
