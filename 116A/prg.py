i = input()
m = 0
t = 0
for j in range(0, int(i)):
    o = [int(k) for k in input().split(' ')]
    t += (o[1] - o[0])
    m = max(m, t)
print(m)