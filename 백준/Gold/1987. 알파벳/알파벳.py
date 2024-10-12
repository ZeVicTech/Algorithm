import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
graph = [input().rstrip() for _ in range(r)]
alphabet = [0 for _ in range(26)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(position):
    global answer
    x, y = position
    alphabet[ord(graph[x][y])-ord("A")] = 1
    answer = max(sum(alphabet), answer)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 > nx or nx > r-1) or (0 > ny or ny > c-1):
            continue
        if alphabet[ord(graph[nx][ny])-ord("A")]:
            continue
        dfs((nx, ny))
    alphabet[ord(graph[x][y])-ord("A")] = 0
        

answer = 0
dfs((0,0))
print(answer)