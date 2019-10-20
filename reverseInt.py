import math

def solution(x):
    sign = -1 if x < 0 else 1
    length = int(math.log(x, 10)) + 1
    temp = None
    for i in range(1,length + 1):
        temp = x % (10 * i )
        x //= (10 * i)
        print(temp)

solution(321)