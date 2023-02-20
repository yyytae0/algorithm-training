def solution(survey, choices):
    dct = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    answer = ''
    for i in range(len(survey)):
        if choices[i] >= 4:
            dct[survey[i][1]] += choices[i] - 4
        else:
            dct[survey[i][0]] += 4 - choices[i]
    if dct['R'] >= dct['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dct['C'] >= dct['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dct['J'] >= dct['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dct['A'] >= dct['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer
