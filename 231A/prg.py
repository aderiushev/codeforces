n = int(input())
m = 0
for k in range(0, n):
    if sum([int(i) for i in input().split(' ')]) >= 2:
        m += 1
print(m)