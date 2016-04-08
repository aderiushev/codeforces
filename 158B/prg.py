n = int(input())
glist = input().split(' ')
g1 = len([int(i) for i in glist if int(i) == 1])
g2 = len([int(i) for i in glist if int(i) == 2])
g3 = len([int(i) for i in glist if int(i) == 3])
g4 = len([int(i) for i in glist if int(i) == 4])

t = g4

tmp_min = min(g1, g3)
g3 -= tmp_min
g1 -= tmp_min
t += tmp_min

t += g2 / 2

t += g3

t += g1 / 4

if not t.is_integer():
    t += 1

print(int(t))