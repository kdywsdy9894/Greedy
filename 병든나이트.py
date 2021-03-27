N, M = map(int, input().split())

def solution(N, M):
    count = 0
    if N >= 3:
        if M >= 7:
            count = 1 + (M-5) + 2
        else: 
            if M >= 4:
                count = 4
            else:
                count = M
    else:
        if N == 2:
            if M >= 7:
                count = 4
            else:
                count = 1+ (M-1)//2
        else:
            count = 1

    return count

print(solution(N, M))








