def solution(cap, n, deliveries, pickups):
    dist = 0
    while True:
        dummy = 0
        post = cap
        rest = cap
        for i in range(n - 1, -1, -1):
            if deliveries[i] or pickups[i]:
                if dummy == 0:
                    dist = dist + (i + 1) * 2
                    dummy = 1
            if deliveries[i] and post:
                if post >= deliveries[i]:
                    post -= deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= post
                    post = 0
            if pickups[i] and rest:
                if rest >= pickups[i]:
                    rest -= pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= rest
                    rest = 0
            if rest == 0 and post == 0:
                break

        if post == cap and rest == cap:
            return dist


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]), 16)
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 30)
print(solution(4, 5, [8, 0, 8, 0, 4], [0, 0, 0, 0, 20]), 50)
print(solution(2, 2, [0, 1], [0, 4]), 8)
print(solution(2, 2, [0, 0], [0, 6]), 12)
print(solution(2, 2, [0, 0], [4, 0]), 4)
print(solution(2, 2, [5, 0], [0, 3]), 10)
print(solution(5, 3, [5, 0, 5], [0, 1, 10]), 16)
print(solution(5, 3, [5, 1, 5], [0, 1, 10]), 16)
print(solution(2, 3, [0, 6, 13], [19, 0, 1]), 54)
print(solution(2, 3, [4, 2, 1], [0, 4, 1]), 16)
print(solution(4, 5, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 12)
print(solution(4, 4, [25, 24, 51, 0], [51, 0, 0, 49]), (13 * 4 + 6 * 2 + 6) * 2)
