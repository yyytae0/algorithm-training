def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    cache = dict()
    cnt = 1
    answer = 0
    for i in cities:
        t = i.lower()
        d = cache.get(t)
        if d and d >= cnt-cacheSize:
            answer += 1
        else:
            answer += 5
        cache[t] = cnt
        cnt += 1
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))