def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    print(sign)
    num1[0], num2[0] = abs(num1[0]), abs(num2[0]) ## This is to adjust the sign for calculation.
    result = [0] * (len(num1) + len(num2))
    print(result)
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            print(result)
            result[i + j] += result[i + j + 1] // 10
            print(result)
            result[i + j + 1] %= 10
            print(result)
    result = result[next((i for i, x in enumerate(result)
                          if x!= 0), len(result)):] or [0]
    print(result)
    return 0

A = [1,2,3]
B = [0,0,0,2]
multiply(A,B)