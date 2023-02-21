def solution(s):
    answer = list(s)
    dummy = 0
    for idx, i in enumerate(answer):
        dummy = 1 - dummy
        if i == ' ':
            dummy = 0
        elif dummy:
            answer[idx] = i.upper()
        else:
            answer[idx] = i.lower()
    return ''.join(answer)