from collections import deque
import sys
import pprint
input = sys.stdin.readline

r,c,t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

purifier = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            purifier.append((i,j))

for _ in range(t):
    graph_temp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 0 or graph[i][j] == -1:
                continue
            center = graph[i][j]
            diffusion = graph[i][j]//5
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if not (0 <= nx < r and 0 <= ny < c) or graph[nx][ny] == -1:
                    continue
                graph_temp[nx][ny] += diffusion
                center -= diffusion
            graph_temp[i][j] += center

    purifier_x,purifier_y = purifier[0]
    
    for i in range(purifier_x,0,-1):
        graph_temp[i][0] = graph_temp[i-1][0]

    for i in range(c-1):
        graph_temp[0][i] = graph_temp[0][i+1]

    for i in range(purifier_x):
        graph_temp[i][c-1] = graph_temp[i+1][c-1]

    for i in range(c-1,0,-1):
        graph_temp[purifier_x][i] = graph_temp[purifier_x][i-1]

    graph_temp[purifier_x][purifier_y] = -1
    graph_temp[purifier_x][purifier_y+1] = 0

    purifier_x,purifier_y = purifier[1]

    for i in range(purifier_x,r-1):
        graph_temp[i][0] = graph_temp[i+1][0]

    for i in range(c-1):
        graph_temp[r-1][i] = graph_temp[r-1][i+1]

    for i in range(r-1,purifier_x,-1):
        graph_temp[i][c-1] = graph_temp[i-1][c-1]

    for i in range(c-1,0,-1):
        graph_temp[purifier_x][i] = graph_temp[purifier_x][i-1]

    graph_temp[purifier_x][purifier_y] = -1
    graph_temp[purifier_x][purifier_y+1] = 0

    graph = graph_temp

result = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            continue
        result+=graph[i][j]

print(result)