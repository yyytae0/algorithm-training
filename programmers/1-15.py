def solution(s):
    answer = 0
    n = len(s)
    cnt1, cnt2 = 0, 0
    dummy = s[0]
    for i in range(n):
        if s[i] == dummy:
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            answer += 1
            cnt1, cnt2 = 0, 0
            if i+1 < n:
                dummy = s[i+1]
    if cnt1 or cnt2:
        answer += 1
    return answer


print(solution('banana'))
print(solution('abracadabra'))
print(solution('aaabbaccccabba'))
