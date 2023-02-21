def solution(s, n):
    answer = ''
    for i in s:
        if i != ' ':
            if i.islower():
                new = ord(i) + n
                while new > 122:
                    new -= 26
            else:
                new = ord(i) + n
                while new > 90:
                    new -= 26
            answer += chr(new)
        else:
            answer += i
    return answer


print(solution("AaZz", 25))
# print(solution("a    b", 1))
# print(solution("a b ", 1))
