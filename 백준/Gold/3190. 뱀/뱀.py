import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    r, c  = map(int, input().split())
    board[r-1][c-1] = 2

l = int(input())
info = []
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))
snake = deque([(0,0)])
board[0][0] = 1
# 순서 오른쪽, 아래, 왼쪽, 위
dir_index = 0
direct = [(0,1), (1,0), (0,-1), (-1,0)]

time = 0
i = 0
while True:
    time += 1
    new_head_x = snake[-1][0] + direct[dir_index][0]
    new_head_y = snake[-1][1] + direct[dir_index][1]
    # 벽에 부딪힐 경우
    if not(0 <= new_head_x < n and 0 <= new_head_y < n):
        break
    # 사과를 먹을 경우
    if board[new_head_x][new_head_y] == 2:
        snake.append((new_head_x, new_head_y))
        board[new_head_x][new_head_y] = 1

    elif board[new_head_x][new_head_y] == 1:
        break

    else:
        snake.append((new_head_x, new_head_y))
        board[new_head_x][new_head_y] = 1
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0
        
    if i < len(info) and time == info[i][0]:
        if info[i][1] == 'D':
            dir_index = (dir_index + 1) % 4
        else:
            dir_index = (dir_index - 1) % 4
        i += 1

print(time)
