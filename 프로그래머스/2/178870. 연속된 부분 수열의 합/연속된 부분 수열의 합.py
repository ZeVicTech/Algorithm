def solution(sequence, k):
    answer = []
    
    n = len(sequence)
    start, end = 0, 0
    sequence_sum = sequence[0]
    sub_sequence_len = n + 1
    answer = [0,0]
    while start < n and end < n:
        
        if k == sequence_sum:
            if sub_sequence_len > end - start + 1:
                sub_sequence_len = end - start + 1
                answer = [start, end]
                
        if k < sequence_sum:
            sequence_sum -= sequence[start]
            start += 1
        else:
            end += 1
            if end < n:
                sequence_sum += sequence[end]
                
    
    return answer