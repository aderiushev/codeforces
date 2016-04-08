from math import ceil
input = input().split(' ')
w = ceil(int(input[0]) / int(input[2]))
h = ceil(int(input[1]) / int(input[2]))
print(w*h);