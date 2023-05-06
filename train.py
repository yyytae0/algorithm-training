from sys import stdin, stdout
import heapq


n = int(stdin.readline())
heap = []
cnt = 0
for i in range(n):
    cnt += 1
    a = int(stdin.readline())
    heapq.heappush(heap, a)
    print(heap)
    if cnt % 2:
        stdout.write(str(heap[cnt//2]) + '\n')
    else:
        stdout.write(str(heap[cnt//2-1]) + '\n')
