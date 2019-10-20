import functools

def intToString(val):
    is_negative = True if val < 0 else False
    s = []
    while val > 0:
        s.append(chr(ord('0') + val % 10))
        #s += str(lsm)
        val //= 10
    return ''.join( s[i] for i in range(len(s)-1,-1,-1))


def string_to_int(s):
    return functools.reduce(
        lambda running_sum, c : running_sum * 10 + string.digits.index(c), s[s[0] == '-'],0) * (-1 if s[0] == '-' else 1
    )

val=314
print(intToString(val))
int1 = "4329"
print(string_to_int(int1))
