from collections import OrderedDict

num = 2020
roman = OrderedDict()
roman[1000]='M'
roman[900]='CM'
roman[500]='D'
roman[400]='CD'
roman[100]='C'
roman[90]='XC'
roman[50]='L'
roman[40]='XL'
roman[10]='X'
roman[9]='IX'
roman[5]='V'
roman[4]='IV'
roman[1]='I'

romVal = ''
while num > 0:
    for i,r in roman.items():
        print(" i= {} r={} n={}".format(str(i), str(r), str(num)))
        while num >= i:
            romVal += r
            num -= i
            print(" val num={} romVal={} num={}".format(str(num), str(romVal), str(num)))
print(romVal)

roman_map = OrderedDict([(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')])
print(roman_map)


