str0 = ''.join(['0' for i in range(0,7)])
str1 = ''.join(['1' for i in range(0,7)])
i = input()
if str0 in i or str1 in i:
    print('YES')
else:
    print('NO')