t = int(input())

for case in range(1, t+1):
    n = int(input())
    a = input()             # 16진수 a를 문자열형태로 입력
    a_num = int(a, 16)      # 16진수 a를 10진법으로 변환
    a_bin = bin(a_num)[2:]  # a를 2집법으로 변환후 2진법 표기인 0b 이후만 추출
    a_len = len(a_bin)
    dp = [0 for _ in range(a_len)]   # dp[i] : i번째 까지 연속된 1의 개수
    dp[0] = int(a_bin[0])   # dp[0] = 2진법 a의 첫자리가 1일 경우 1 0일 경우 0을 입력
    ans = 0                 # 최대값을 저장할 변수
    for i in range(1, a_len):
        if a_bin[i] == '1':       # 2진법 a의 i번째 자리가 1일 경우
            dp[i] = dp[i-1] + 1   # 직전까지 연속된 1의 개수 +1
        else:
            dp[i] = 0             # 0일 경우 연속된 1의 개수는 0
        if dp[i] > ans:
            ans = dp[i]           # [i]번째까지 연속된 1의 개수가 ans보다 클 경우 ans 최신화
    print(f'#{case} {ans}')
