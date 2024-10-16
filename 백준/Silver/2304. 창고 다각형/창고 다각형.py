import sys
input = sys.stdin.readline

n = int(input())
pillar = [0 for _ in range(1001)]
for _ in range(n):
    position, height = map(int, input().split())
    pillar[position] = height

left_scaned = [0 for _ in range(1001)]
max_height = 0
# 왼쪽부터 스캔
for i in range(1001):
    if max_height < pillar[i]:
        max_height = pillar[i]
    left_scaned[i] = max_height

right_scaned = [0 for _ in range(1001)]
max_height = 0
for i in range(1001):
    if max_height < pillar[1000 - i]:
        max_height = pillar[1000 - i]
    right_scaned[1000 - i] = max_height

answer = 0
for i in range(1001):
    answer += min(left_scaned[i], right_scaned[i])

print(answer)

