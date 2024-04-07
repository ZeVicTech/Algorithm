import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot_position = deque([0 for _ in range(n)])
cnt = 0

def rotate(belt, robot_position):
    temp = belt.pop()
    belt.appendleft(temp)
    robot_position.pop()
    robot_position.appendleft(0)
    # 내리는 위치에 로봇이 도달할 경우 바로 내림
    robot_position[-1] = 0

    return belt, robot_position

def move_robot(belt, robot_position, cnt):
    for i in range(n-1, -1, -1):
        if robot_position[i] == 0:
            continue
        if robot_position[i+1] == 0 and belt[i+1] >= 1:
            robot_position[i+1] = 1
            robot_position[i] = 0
            belt[i+1] -= 1
            if i == n-1:
                robot_position[i+1] = 0
            if belt[i+1] == 0:
                cnt += 1

    return belt, robot_position, cnt

def upload_robot(belt, robot_position, cnt):
    if belt[0] == 0:
        return belt, robot_position, cnt
    belt[0] -= 1
    robot_position[0] = 1
    if belt[0] == 0:
        cnt += 1

    return belt, robot_position, cnt

i = 0
while cnt < k:
    i+=1
    belt, robot_position = rotate(belt, robot_position)
    belt, robot_position, cnt = move_robot(belt, robot_position, cnt)
    belt, robot_position, cnt = upload_robot(belt, robot_position, cnt)

print(i)
