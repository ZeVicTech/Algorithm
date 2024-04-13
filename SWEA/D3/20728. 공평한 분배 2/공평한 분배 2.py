t = int(input())

for i in range(t):
    n , k = map(int, input().split())
    candy = list(map(int, input().split()))
    candy.sort()
    min_diff = int(1e9)
    for j in range(n-k+1):
        min_diff = min(candy[j+k-1] - candy[j], min_diff)

    print(f'#{i+1} {min_diff}')