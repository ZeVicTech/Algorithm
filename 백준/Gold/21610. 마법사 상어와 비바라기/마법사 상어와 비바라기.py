import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(n)]
move = []
cloud_map = [[0 for _ in range(n)] for _ in range(n)]
cloud_map[n-1][0] = 1
cloud_map[n-1][1] = 1
cloud_map[n-2][0] = 1
cloud_map[n-2][1] = 1
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)] # 초기 구름

for _ in range(m):
    move.append(tuple(map(int, input().split())))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def move_cloud(direct, distance):
    global cloud, cloud_map
    cloud_map_temp = [[0 for _ in range(n)] for _ in range(n)]
    cloud_temp = []
    for x, y in cloud:
        nx = (x + dx[direct] * distance) % n
        ny = (y + dy[direct] * distance) % n

        if nx < 0:
            nx = n + nx -1
        if ny < 0:
            ny = n + ny -1

        # 이동한 위치에 구름 생성
        cloud_map_temp[nx][ny] = 1
        cloud_temp.append((nx,ny))
        water[nx][ny] += 1
    cloud = cloud_temp
    cloud_map = cloud_map_temp

def increment_water():
    global water
    for x, y in cloud:
        for i in range(8):
            if i % 2 == 0:
                continue
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if water[nx][ny] != 0:
                water[x][y] += 1

def create_cloud():
    global cloud, cloud_map
    cloud_map_temp = [[0 for _ in range(n)] for _ in range(n)]
    cloud_temp = []
    for i in range(n):
        for j in range(n):
            if cloud_map[i][j] == 1:
                continue
            if water[i][j] < 2:
                continue
            cloud_map_temp[i][j] = 1
            cloud_temp.append((i,j))
            water[i][j] -= 2

    # 새로운 구름 생성
    cloud = cloud_temp
    cloud_map = cloud_map_temp

for direct, distance in move:
    move_cloud(direct-1, distance)
    increment_water()
    create_cloud()

result = 0
for i in range(n):
    result += sum(water[i])

print(result)