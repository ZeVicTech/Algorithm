import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

routes = list([int(1e9)] * n for _ in range(n))

for i in range(n):
    for j in range(n):
        if i == j:
            routes[i][j] = 0

for _ in range(m):
    start, end, cost = map(int,input().split())
    if routes[start-1][end-1] > cost:
        routes[start-1][end-1] = cost

for k in range(n):
    for i in range(n):
        for j in range(n):
            routes[i][j] = min(routes[i][j], routes[i][k]+routes[k][j])

for i in range(n):
    for j in range(n):
        value = routes[i][j]
        if value != int(1e9):
            print(value, end = ' ')
        else:
            print(0, end =' ')
    print()