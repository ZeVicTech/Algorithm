import sys
input = sys.stdin.readline

n, s = map(int, input().split())
sequence = list(map(int, input().split()))
cum_seq = []

for i in range(0, n):
    if i == 0:
        cum_seq.append(sequence[0])
    else:
        cum_seq.append(sequence[i] + cum_seq[i-1])

cum_seq = [0] + cum_seq
answer = int(1e9)
left, right = 0, 1
while left <= right:
    diff = cum_seq[right] - cum_seq[left]

    if diff >= s:
        answer = min(answer, right - left)
        left += 1
    else:
        right += 1
        if right == n+1:
            break
if answer == int(1e9):
    print(0)
else:
    print(answer)