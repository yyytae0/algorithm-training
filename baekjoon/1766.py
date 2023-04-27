import heapq


def check():
    while heap:
        v = heapq.heappop(heap)
        print(v, end=' ')
        for i in lst[v]:
            temp[i] -= 1
            if not temp[i]:
                heapq.heappush(heap, i)


n, m = map(int, input().split())
temp = [0 for _ in range(n+1)]
lst = [[] for _ in range(n+1)]
heap = []
for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    temp[b] += 1
for i in range(1, n+1):
    if not temp[i]:
        heapq.heappush(heap, i)
check()
