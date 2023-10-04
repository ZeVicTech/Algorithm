import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
chick = []
houses = []
result = int(1e9)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chick.append((i,j))
        elif graph[i][j] == 1:
            houses.append((i,j))

combs = combinations(chick, m)

for comb in combs:
    sum = 0
    for house_x, house_y in houses:
        temp = int(1e9)
        for chick_x, chick_y in comb:
            temp = min(temp, abs(house_x - chick_x) + abs(house_y-chick_y))
        sum += temp
    result = min(result,sum)

print(result)