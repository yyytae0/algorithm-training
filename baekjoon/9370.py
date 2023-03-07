from sys import stdin


ip = int(stdin.readline())

for case in range(ip):
    n, m, t = map(int, stdin.readline().split())
    s, g, h = map(int, stdin.readline().split())
    dct = dict()
    for i in range(1, n):
        dct[i] = []
    for i in range(m):
        a, b, d = map(int, stdin.readline().split())
        dct[a].append([b, d])
        dct[b].append([a, d])
    d =
