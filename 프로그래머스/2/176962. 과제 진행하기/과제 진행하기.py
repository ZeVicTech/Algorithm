def solution(plans):
    
    for i in range(len(plans)):
        h, w = map(int, plans[i][1].split(':'))
        plans[i][1] = h * 60 + w
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key=lambda x: x[1])
    
    stack = []
    answer = []
    for i in range(len(plans)-1):
        stack.append([plans[i][0], plans[i][2]])
        gap = plans[i+1][1] - plans[i][1]
        
        while stack and gap:
            name, playtime = stack.pop()
            
            if playtime > gap:
                playtime -= gap
                gap = 0
                stack.append([name, playtime])
            else:
                gap -= playtime
                answer.append(name)
                
    answer.append(plans[-1][0])
    print(answer)
    
    for i in range(1, len(stack) + 1):
        answer.append(stack[-i][0])

    return answer