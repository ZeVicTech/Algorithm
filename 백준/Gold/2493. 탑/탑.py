import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
# 타원의 높이, 인덱스 순
stack = [(towers[0], 0)]
answer = [0]

for i in range(1, len(towers)):
    if stack[-1][0] >= towers[i]:
        answer.append(stack[-1][1]+1)
        stack.append((towers[i],i))
    else:
        while stack and stack[-1][0] <= towers[i]:
            stack.pop()
        if stack:
            answer.append(stack[-1][1]+1)
        else:
            answer.append(0)
        stack.append((towers[i],i))

print(' '.join(map(str, answer)))

