import sys
input = sys.stdin.readline

n = int(input())
info = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    count = 0
    taller = info[i]
    for j in range(n):
        if count == taller and answer[j] == 0:
            answer[j] = i + 1
            break
        if answer[j] == 0:
            count+=1

print(" ".join(map(str, answer)))