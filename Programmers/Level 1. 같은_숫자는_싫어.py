def solution(arr):
    ans = []
    ans.append(arr[0])
    cur = arr[0]
    
    for i in arr:
        if i != cur:
            ans.append(i)
            cur = i
            
    return ans