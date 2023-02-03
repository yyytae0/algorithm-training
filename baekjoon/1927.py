from sys import stdin, stdout
import heapq

ip = int(stdin.readline())
heap = []
cnt = 0
for i in range(ip):
    task = int(stdin.readline())
    if task == 0:
        if cnt == 0:
            stdout.write('0\n')

        else:
            stdout.write(str(heapq.heappop(heap)) + '\n')
            cnt -= 1

    else:
        heapq.heappush(heap, task)
        cnt += 1
