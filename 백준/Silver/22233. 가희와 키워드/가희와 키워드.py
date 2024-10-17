import sys
inpyt = sys.stdin.readline

n, m = map(int, input().split())
memo = set(input().rstrip() for _ in range(n))

for _ in range(m):
    post = input().rstrip().split(',')
    for keyword in post:
        if keyword in memo:
            memo.remove(keyword)

    print(len(memo))
