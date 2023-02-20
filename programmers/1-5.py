def solution(new_id):
    answer = ''
    lst = list(new_id)
    for idx, i in enumerate(lst):
        if i.isupper():
            lst[idx] = i.lower()
        if i.isdigit() or i.isupper() or i.islower() or i == '-' or i == '_' or i == '.':
            continue
        else:
            lst[idx] = ''
    cnt = 0
    s = 0
    for idx, i in enumerate(lst):
        if i == '.':
            if cnt:
                lst[idx] = ''
            cnt += 1
        elif i == '':
            continue
        else:
            cnt = 0

    answer = ''.join(lst)
    if answer[0] == '.' and answer[-1] == '.':
        answer = answer[1:-1]
    elif answer[0] == '.':
        answer = answer[1:]
    elif answer[-1] == '.':
        answer = answer[:-1]

    if not answer:
        answer = 'a'

    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    while len(answer) < 3:
        answer += answer[-1]

    return answer
