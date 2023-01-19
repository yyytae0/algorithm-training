def change_switch(s, n, switch):
    switch_new = switch[:]
    if s == 1:
        for i in range(n-1, len(switch), n):
            switch_new[i] = 1 - switch_new[i]
        return switch_new

    else:
        switch_new[n-1] = 1 - switch_new[n-1]
        for i in range(1, len(switch)//2):
            if (n - 1 - i < 0) or (n - 1 + i >= len(switch)):
                break

            else:
                if switch[n-1-i] == switch[n-1+i]:
                    switch_new[n-1-i] = 1 - switch_new[n-1-i]
                    switch_new[n-1+i] = 1 - switch_new[n-1+i]
                else:
                    break



        return switch_new


num = int(input())
switch = list(map(int, input().split()))
student = int(input())
student_lst = list()

for i in range(student):
    student_lst.append(list(map(int, input().split())))

for i in student_lst:
    switch = change_switch(i[0], i[1], switch)

while len(switch) != 0:
    if len(switch) > 20:
        print(*switch[:20])
        switch = switch[20:]

    else:
        print(*switch)
        switch = []
