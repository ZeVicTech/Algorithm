import sys
from copy import deepcopy
from collections import deque

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0,0))
    visited_temp = deepcopy(visited)
    visited_temp[0][0] = 1

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] == 1:
                visited_temp[nx][ny] += 1
                continue
            if visited_temp[nx][ny] == 0:
                q.append((nx, ny))
                visited_temp[nx][ny] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited_temp[i][j]>=2:
                graph[i][j] = 0


def is_cheese_disappear():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                return False
    
    return True

answer = 0
while True:
    bfs()
    answer+=1
    if is_cheese_disappear():
        break

print(answer)


