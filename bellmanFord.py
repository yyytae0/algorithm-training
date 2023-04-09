def bellmanford(start):
    # 최단거리 테이블 초기화
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0

    # 1 ~ n-1개의 노드를 사용한 최단거리 구하기 루프
    for i in range(n-1):
        for a, b, c in lst:
            if dist[a] != float('inf') and dist[a]+c < dist[b]:
                dist[b] = dist[a] + c

    # 음의 사이클 확인
    cycle = 0
    for a, b, c in lst:
        if dist[a] != float('inf') and dist[a] + c < dist[b]:
            print("negative")
            cycle = 1
            break

    if cycle == 0:
        for i in range(1, len(dist)):
            print(i, dist[i])


n, m = map(int, input().split())
lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))
bellmanford(1)
