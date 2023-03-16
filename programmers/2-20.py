import math


def solution(fees, records):
    answer = dict()
    IN = dict()
    for i in records:
        a, b, c = i.split()
        a = int(a[:2])*60 + int(a[3:])
        if c == 'IN':
            IN[b] = a
        else:
            d = a - IN[b]
            del IN[b]
            if answer.get(b):
                answer[b] += d
            else:
                answer[b] = d
    for i in IN:
        d = 1439 - IN[i]
        if answer.get(i):
            answer[i] += d
        else:
            answer[i] = d
    lst = []
    for i in answer:
        lst.append((i, answer[i]))
    lst.sort()
    ans = []
    for i in lst:
        cost = fees[1]
        if i[1] > fees[0]:
            cost += math.ceil((i[1] - fees[0]) / fees[2]) * fees[3]
        ans.append(cost)
    return ans


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))