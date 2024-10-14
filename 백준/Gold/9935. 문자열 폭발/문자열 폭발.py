import sys
input = sys.stdin.readline

sequence = input().rstrip()
target = input().rstrip()

stack = []
for i in range(len(sequence)):
    stack.append(sequence[i])
    if "".join(stack[-len(target):]) == target:
        for _ in range(len(target)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))

