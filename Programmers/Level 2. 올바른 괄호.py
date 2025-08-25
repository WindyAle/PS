def solution(s):
    answer = True
    bracket = []
    
    for ch in s:
        if ch == '(':
            bracket.append(ch)
        else:
            # ch ==')'
            if bracket:
                bracket.pop()
            else:
                answer = False

    if bracket:
        answer = False
    
    return answer

s = '())'
print(solution(s))