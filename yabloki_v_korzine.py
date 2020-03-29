p = int(input())
a = int(input())
print('not greater than 10000')
if a <= 10000:
    res = a - ((a // p) * p)
    print('There are apples in the basket' + ' ' + '=' +' ' + str(res))
else:
    print('Error')
