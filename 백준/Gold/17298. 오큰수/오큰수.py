import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

stack = []
nge = [-1 for _ in range(n)]

for i in range(n):

    while stack and a[stack[-1]] < a[i]:
        index = stack.pop()
        nge[index] = a[i]

    stack.append(i)

print(*nge)