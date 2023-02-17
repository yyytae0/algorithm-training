def check(n):
    for i in range(3, int(n**(1/2)), 2):
        if not n%i:
            return False
    return True
