def solution(nums):
    check = [0 for _ in range(200001)]
    cnt = 0
    for i in nums:
        if not check[i]:
            cnt += 1
            check[i] = 1
    answer = min(len(nums)//2, cnt)
    return answer