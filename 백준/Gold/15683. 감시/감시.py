import sys
from copy import deepcopy
from pprint import pprint
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
num = 0
wall = 0
cctv = []

# 동 남 서 북 순
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def four_number(number, direct):
    i = 0
    while number >= 4:
        direct[i] = number % 4
        number //= 4
        i += 1
    direct[i] = number
    return direct

def fill(x, y, mode, graph):
    while True:
        x = x + dx[mode]
        y = y + dy[mode]
        if not(0 <= x < n and 0 <= y < m) or graph[x][y] == 6:
            break
        # cctv가 있는 자리일 경우
        if graph[x][y] != 0:
            continue
        graph[x][y] = -1

def check(graph):
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                result += 1
    return result
wall = 0
# cctv 정보 파악
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            continue
        if graph[i][j] == 6:
            wall += 1
            continue
        cctv.append([i, j, graph[i][j]])
        num += 1

direct = [0] * 8
answer = n*m - wall
for i in range(4**num):
    graph_temp = deepcopy(graph)
    direct = four_number(i, direct)

    for j in range(num):
        x, y, c = cctv[j]
        if c == 1:
            fill(x, y, direct[j], graph_temp)
        elif c == 2:
            fill(x, y, direct[j], graph_temp)
            fill(x, y, (direct[j] + 2) % 4, graph_temp)
        elif c == 3:
            fill(x, y, direct[j], graph_temp)
            fill(x, y, (direct[j] + 3) % 4, graph_temp)
        elif c == 4:
            fill(x, y, direct[j], graph_temp)
            fill(x, y, (direct[j] + 2) % 4, graph_temp)
            fill(x, y, (direct[j] + 3) % 4, graph_temp)
        else:
            fill(x, y, direct[j], graph_temp)
            fill(x, y, (direct[j] + 1) % 4, graph_temp)
            fill(x, y, (direct[j] + 2) % 4, graph_temp)
            fill(x, y, (direct[j] + 3) % 4, graph_temp)
    answer = min(answer, check(graph_temp))
    
print(answer)

