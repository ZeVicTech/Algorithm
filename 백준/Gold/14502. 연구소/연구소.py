import sys
from collections import deque
from copy import deepcopy
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
virus = []
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i,j))

def bfs(graph):
    q = deque(virus)
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0<=nx<n and 0<=ny<m):
                continue
            if graph[nx][ny] == 1 or graph[nx][ny] == 2:
                continue
            graph[nx][ny] = 2
            q.append((nx,ny))

    result = 0
    for i in range(n):
        result += graph[i].count(0)

    return result

def make_wall(cnt):
    # 벽이 3개 세워졌을 경우 bfs 실행
    if cnt == 3:
        global answer
        answer = max(bfs(deepcopy(graph)),answer)
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt+1)
                graph[i][j] = 0

make_wall(0)

print(answer)