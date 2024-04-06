import sys
input = sys.stdin.readline

n, m = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]
cloud = [(n-1,0), (n-1,1), (n-2, 0), (n-2, 1)] # 초기 구름

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def move_cloud(direct, distance):
    cloud_temp = set()
    for x, y in cloud:
        nx = (x + dx[direct] * distance) % n
        ny = (y + dy[direct] * distance) % n

        cloud_temp.add((nx,ny))
        water[nx][ny] += 1
    return cloud_temp

def copy_water():
    global water
    for x, y in cloud:
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if water[nx][ny] != 0:
                water[x][y] += 1

def create_cloud():
    cloud_temp = set()
    for i in range(n):
        for j in range(n):
            if (i,j) in cloud:
                continue
            if water[i][j] < 2:
                continue
            cloud_temp.add((i,j))
            water[i][j] -= 2

    # 새로운 구름 생성
    return cloud_temp

for direct, distance in move:
    cloud = move_cloud(direct-1, distance)
    copy_water()
    cloud = create_cloud()

result = 0
for i in range(n):
    result += sum(water[i])

print(result)