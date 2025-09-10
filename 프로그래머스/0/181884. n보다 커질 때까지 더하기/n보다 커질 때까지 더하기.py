def solution(numbers, n):
    ret = 0
    i = 0
    
    while ret <= n:
        ret += numbers[i]
        i += 1
        
    return ret