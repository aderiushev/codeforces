i = int(input())
r = {}
for j in range(0, i):
    n = input()
    if n in r:
        r[n] += 1
        print(n + str(r[n] - 1))
    else:
        r[n] = 1
        print('OK')