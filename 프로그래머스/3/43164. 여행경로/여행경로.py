def solution(tickets):
    # 1. 알파벳 순서가 앞서는 경로를 찾기 위해 티켓 자체를 미리 정렬합니다.
    tickets.sort() 
    
    # 2. 각 티켓의 사용 여부를 체크할 배열을 만듭니다. (티켓 개수만큼 False)
    visited = [False] * len(tickets)
    answer = []
    
    # 재귀 함수 정의: dfs(현재 공항, 지금까지의 경로)
    def dfs(airport, path):
        nonlocal answer
        
        # 이미 정답을 하나라도 찾았다면? 
        # (티켓이 정렬되어 있으므로 처음 찾은 정답이 무조건 알파벳 순으로 가장 앞섭니다)
        if answer:
            return
            
        # 3. 종료 조건: 모든 티켓을 다 썼을 때 (경로의 길이는 티켓 수 + 1)
        if len(path) == len(tickets) + 1:
            answer = path # 정답을 저장하고 탐색 종료
            return
            
        # 4. 현재 공항에서 출발하는 남은 티켓을 찾습니다.
        for i in range(len(tickets)):
            start, end = tickets[i]
            
            # 현재 공항과 출발지가 같고, 아직 안 쓴 티켓이라면?
            if start == airport and not visited[i]:
                visited[i] = True           # 티켓 사용 (방문 처리)
                dfs(end, path + [end])      # 도착지 공항으로 이동하여 다시 탐색 (재귀)
                
                # 5. 백트래킹: 위 dfs 탐색이 실패하고 돌아왔다면, 
                # 다른 경로를 찾아봐야 하므로 방금 쓴 티켓을 다시 취소합니다.
                visited[i] = False          

    # 항상 "ICN"에서 출발
    dfs("ICN", ["ICN"])
    
    return answer