import functools

def test(x):
    return functools.reduce(lambda sum, i : sum + i, range(5),23)

print(test(5))

s = "Hello"
m = "manish"
print((lambda sum, i: sum + i * i, range(5)))