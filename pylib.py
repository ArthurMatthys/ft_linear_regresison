def is_float(s):
    try:
        a = float(s)
    except ValueError:
        return False
    else:
        return True


def is_int(s):
    try:
        a = float(s)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


def abs(x):
    if not (is_int(x) or is_float(x)):
        print ("ABS : type error")
        return -1
    else:
        if x < 0:
            return -x
        else:
            return x


def pow_int(x, y):
    if not (is_int(x) or is_float(x)) or is_int(y):
        print ("ABS : type error")
        return -1
    else:
        while y > 1:
            x *= x
            y -= 1
    return x


def sqrt(x, prec):
    if not (is_float(x) or is_int(x)):
        print ("SQRT : type error")
        return -1
    elif x < 0:
        print ("SQRT : Negative value")
        return -1
    else:
        i = 0
        j = x
        while abs(i - j) > prec:
            mid = (i + j) / 2
            if pow_int(mid, 2) > x:
                j = mid
            else:
                i = mid
    return i


def sum(t):
    tot = 0
    for i in t:
        tot += i
    return tot


def check_file(str):
    try:
        f = open(str, 'r')
    except FileNotFoundError:
        return False
    else:
        f.close()
        return True
