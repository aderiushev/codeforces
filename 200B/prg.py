i = int(input())
n = [int(j) for j in input().split(' ')]
print('{0:.12f}'.format(sum(n) / i))