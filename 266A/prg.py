i = int(input())
s = input()
f = ['RR', 'GG', 'BB']
r = 0
for i in f:
    try:
        while True:
            idx = s.index(i)
            s = s[:idx] + s[idx+1:]
            r += 1
    except ValueError as e:
        pass
print(r)