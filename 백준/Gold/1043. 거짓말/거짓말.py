n,m = map(int,input().split()) # n은 사람수, m은 파티의 수
truth = set(input().split()[1:])
parties = [input().split()[1:] for _ in range(m)]

# 파티를 순회하며 진실을 알고 있는 사람 갱신
for _ in range(m):
    for party in parties:
        for person in party:
            if person in truth:
                truth = truth.union(party)
                break

cnt = 0
for party in parties:
    for person in party:
        if person in truth:
            cnt += 1
            break

print(m-cnt)
