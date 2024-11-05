def solution(picks, minerals):
    
    total_digging_count = 0
    mineral_sorting = []
    
    for p in picks:
        total_digging_count += 5 * p
    
    total_digging_count = min(total_digging_count, len(minerals))
        
    diamond_count, iron_count, stone_count = 0, 0, 0
        
    for i in range(total_digging_count):
        if minerals[i] == "diamond":
            diamond_count += 1
        elif minerals[i] == "iron":
            iron_count += 1
        elif minerals[i] == "stone":
            stone_count += 1
            
        if (i + 1) % 5 == 0 or (i + 1) == total_digging_count:
            mineral_sorting.append((diamond_count, iron_count, stone_count))
            diamond_count, iron_count, stone_count = 0, 0, 0
            
    mineral_sorting.sort(key = lambda x: (x[0],x[1],x[2]), reverse=True)
    
    answer = 0
    for m in mineral_sorting:
        if picks[0] != 0:
            answer += sum(m)
            picks[0] -= 1
        elif picks[1] != 0:
            answer += 5 * m[0] + m[1] + m[2]
            picks[1] -= 1
        else:
            answer += 25 * m[0] + 5 * m[1] + m[2]
            picks[2] -= 1
            
    return answer