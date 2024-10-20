from pprint import pprint
from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[0 for i in range(m)] for j in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    result = [0 for _ in range(m)]
    
    def bfs(start):
        a, b = start
        visited[a][b] = 1
        q = deque([start])
        oil_column = set()
        oil_column.add(b)
        count = 1
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not(0 <= nx <= n-1 and 0<= ny <= m-1):
                    continue
                if visited[nx][ny] == 1 or land[nx][ny] == 0:
                    continue
                visited[nx][ny] = 1
                q.append((nx, ny))
                oil_column.add(ny)
                count += 1
        
        for c in oil_column:
            result[c] += count
                
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs((i, j))
    
    return max(result)