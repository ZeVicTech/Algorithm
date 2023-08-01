import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * n for _ in range(n)] # 팰린드롬 여부를 저장하는 dp 테이블
sequence = list(map(int,input().split()))

for i in range(n):# 길이가 1인 팰린드롬 수를 찾아서 dp 테이블 갱신
    dp[i][i] = 1

for i in range(n-1):# 길이가 2인 팰린드롬 수를 찾아서 dp 테이블 갱신
    if sequence[i] == sequence[i+1]:
        dp[i][i+1] = 1

for num_len in range(2,n): # 길이가 3이상인 팰린드롬 수를 찾아서 dp 테이블 갱신
    for start in range(n-num_len):
        end = start + num_len
        if dp[start+1][end-1] == 1 and sequence[start] == sequence[end]:
            dp[start][end] = 1

m = int(input())
for _ in range(m):
    s,e = map(int,input().split())
    print(dp[s-1][e-1])