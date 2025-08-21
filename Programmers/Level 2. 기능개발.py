def solution(progresses, speeds):
    answer = []
    cnt = 0

    while progresses:
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)

        if cnt:
            answer.append(cnt)

        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        cnt = 0
                
    return answer