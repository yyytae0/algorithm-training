# 짝수의 경우 : a2n = an(an+2*an-1)
#
# 홀수의 경우 : a2n-1 = (an)**2+(an-1)**2

def check(n):
    if n % 2:
        return check((n+1)//2)**2 + check((n+1)//2 - 1)**2
        pass
    else:
        pass


n = int(input())
