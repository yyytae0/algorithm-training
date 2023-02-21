def solution(nums):
    answer = 0
    n = len(nums)
    prime = [1 for _ in range(3000)]
    prime[0], prime[1] = 0, 0
    for i in range(2, 55):
        if prime[i]:
            for j in range(2, 1500):
                if i*j < 3000:
                    prime[i*j] = 0
                else:
                    break
    dummy = 0
    for i in range(n):
        dummy += nums[i]
        for j in range(i+1, n):
            dummy += nums[j]
            for k in range(j+1, n):
                dummy += nums[k]
                if prime[dummy]:
                    answer += 1
                dummy -= nums[k]
            dummy -= nums[j]
        dummy -= nums[i]

    return answer
