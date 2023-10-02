from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

x,y = 0,0
baby_shark = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x,y = i,j

def bfs(a,b,baby_shark):
    visited = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((a,b))
    visited[a][b] = 0
    temp = []

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] <= baby_shark:
                    q.append((nx,ny));
                    visited[nx][ny] = visited[x][y] + 1
                    if graph[nx][ny] < baby_shark and graph[nx][ny] != 0:
                        temp.append((visited[nx][ny], nx, ny))

    return sorted(temp, key = lambda x: (x[0], x[1], x[2]))

cnt = 0
check = 0
while True:
    value = bfs(x,y,baby_shark)
    if len(value) == 0:
        break
    time,nx,ny = value[0]
    graph[x][y] = 0 #물고기가 있던 자리
    graph[nx][ny] = 0 #상어가 있던 자리
    x,y = nx,ny
    cnt += time
    check += 1
    if check == baby_shark:
        check = 0
        baby_shark += 1

print(cnt)