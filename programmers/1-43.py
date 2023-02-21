def solution(arr1, arr2):
    answer = []
    n1 = len(arr1[0])
    n2 = len(arr1)
    for i in range(n2):
        dummy = []
        for j in range(n1):
            dummy.append(arr1[i][j] + arr2[i][j])
        answer.append(dummy)
    return answer
