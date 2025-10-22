def solution(strArr):
    return [str.upper() if i & 1 else str.lower() for i, str in enumerate(strArr)]