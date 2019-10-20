def is_Palindrome(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def is_Palindrome_Pyythonic(s):
    return all( a == b for a,b in zip(
        map(str.lower,filter(str.isalnum,s)),
        map(str.lower, filter(str.isalnum, reversed(s)))
        ))

def snake_string_pythonic(c):
    return c[1::4] + c[::2] + c[3::4]

print(snake_string_pythonic("Hello World!"))

print(is_Palindrome('madam'))
print(is_Palindrome_Pyythonic("A man, a plan, a canal, Panama"))

inString = "A man7, a plan, a canal, Pa7nama"
for a,b in zip(
    map(str.lower, filter(str.isalnum, inString)),
    map(str.lower, filter(str.isalnum, reversed(inString)))
):
    pass#print(a + " " + b)

for i in map(str.upper,filter(str.isalnum, inString)):
  pass #print(i)

a = list(filter(str.isalnum, inString))
print(a)

b = list(map(str.lower,filter(str.isalnum, inString)))
print(b)

