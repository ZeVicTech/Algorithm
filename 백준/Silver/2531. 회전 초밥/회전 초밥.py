import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

sushi_list = []
for _ in range(n):
    sushi_num = int(input())
    sushi_list.append(sushi_num)
sushi_list = sushi_list * 2

max_num = 0
for i in range(n):
    temp = set(sushi_list[i:i+k])
    temp.add(c)
    max_num = max(max_num, len(temp))

print(max_num)