import heapq


def solution(n, k, enemy):
    answer = 0
    heap_mx = list()
    for i in enemy:
        answer += 1
        heapq.heappush(heap_mx, (-i, i))
        n -= i
        while n < 0:
            if k == 0:
                break
            k -= 1
            n += heapq.heappop(heap_mx)[1]
        if n < 0:
            answer -= 1
            return answer
    return answer
