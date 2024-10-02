import sys
input = sys.stdin.readline

seq = input().rstrip()

# 윈도우 사이즈는 연속된 a의 길이가 될 예정
window_size = 0

# 문자열 안에 들어있는 a의 개수
for s in seq:
    if s != 'a':
        continue
    window_size += 1

seq_length = len(seq)

answer = int(1e9)

for i in range(seq_length + window_size):
    count = 0
    for j in range(i, i+window_size):
        if seq[j%seq_length] == 'b':
            count += 1
    answer = min(answer, count)

print(answer)

