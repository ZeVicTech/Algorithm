def solution(targets):
    targets.sort(key=lambda x : x[1])
    s, e = 0, 0
    
    count = 0
    for target in targets:
        if target[0] >= e:
            e = target[1]
            count += 1
            
    return count