from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            break

        for i in [v-1, v+1, v*2]:
            if 0 <= i <= mx and not lst[i]:
                lst[i] = lst[v] + 1
                q.append(i)


n, k = map(int, input().split())
mx = 10**5
lst = [0 for _ in range(mx+1)]
bfs()
print(lst[k])
