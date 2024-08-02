import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def is_available(line: list, visited: list) -> bool:
    cnt = 1
    for i in range(1, n):
        if line[i-1] == line[i]:
            cnt+=1
        elif line[i-1]+1 == line[i] and cnt >= l and visited[i-l:i] == [False]*l:
            cnt = 1
            visited[i-l:i] = [True]*l
        elif line[i-1] > line[i]:
            cnt=1
        else:
            return False
    
    return True

result = 0

for _ in range(2):
    for line in graph:
        visited = [False] * len(line)

        if is_available(line, visited) and is_available(line[::-1], visited[::-1]):
            result += 1

    graph = list(map(list, zip(*graph)))

print(result)