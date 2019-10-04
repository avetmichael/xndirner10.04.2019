def ex_201(n):
    b = 0
    while n != 0:
        a = n % 10
        n = int(n / 10)
        b = b + 1
    return b
print(ex_201(312144121241321))
#########
def ex_202(n):
    x = 0
    while n != 0:
        b = n % 10
        n = int(n / 10)
        x = x + b
    return x
print(ex_202(4121348))
###########
def ex_203(n):
    a = 1
    while n != 0:
        b = n % 10
        n = n // 10
        a = a * b
    return a
print(ex_203(5424))
###########
def ex_204(n):
    b = 0
    while n != 0:
        b = n % 10
        n = n // 10
        print(b, ',', end=' ')
    print()
ex_204(6851)
########
def ex_205(n):
    b = 0
    while n != 0:
        x = n % 10
        b = b * 10
        b = b + x
        n = int(n / 10)
    while b != 0:
        e = b % 10
        b = int(b / 10)
        print(str(e) + ',', end=' ')
    print()
ex_205(4567)
##########
def ex_206(n):
    c = 0
    while n != 0:
        y = n % 10
        c = c * 10
        c = c + y
        n = int(n / 10)
    return c
print(ex_206(4321))
############
def ex_207(n):
    while n != 0:
        y = n % 10
        n = n // 10
        if y == 2:
            return True
    return False
print(ex_207(1267))
##########
def ex_208(n):
    c = 0
    while n != 0:
        y = n % 10
        c = c * 10
        c = c + y
        n = int(n / 10)
        if c == n:
            return True
    return False
print(ex_208(1221))
##############
def ex_209(n):
    while n != 0:
        z = n % 10
        n = int(n / 10)
        if z % 2 == 1:
            return True
    return False
print(ex_209(2467))
############
def ex_210(n):
    a = 0
    b = 0
    while n != 0:
       x = n % 10
       n = n // 10
       if x % 2 == 1:
           a = a+ x
       if x % 2 == 0:
           b = b + x
       if a == b:
           return True
    return False
print(ex_210(52361))




