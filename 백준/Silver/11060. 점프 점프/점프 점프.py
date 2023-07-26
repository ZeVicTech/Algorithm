import sys
input = sys.stdin.readline

n = int(input())
maze = list(map(int,input().split()))
dp = [1000]*n
dp[0] = 0 # 처음에는 점프없이 도달 가능
for i in range(n):
    for j in range(i+1,i + maze[i] + 1): # 인덱스 i 위치에서 점프가 가능한 범위까지 탐색
        if j == n:# 미로 범위를 벗어날 경우 break
            break
        dp[j] = min(dp[j], dp[i]+1) # 해당 위치에 도달하기까지의 횟수중 작은 값으로 갱신

if dp[n-1] == 1000: # 도달못하는 경우 -1 출력
    print(-1)
else:
    print(dp[n-1])