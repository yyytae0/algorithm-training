def solution(arr):
    answer = []
    dummy = 10
    for i in arr:
        if i != dummy:
            answer.append(i)
            dummy = i
    return answer