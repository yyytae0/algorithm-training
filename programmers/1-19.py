def solution(food):
    total = 0
    for i in food:
        total += i
    ans = ['' for _ in range(total)]
    ans[(total//2)] = '0'
    idx = 0
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            ans[idx] = str(i)
            ans[-idx-1] = str(i)
            idx += 1
    answer = ''.join(ans)
    return answer


print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))
