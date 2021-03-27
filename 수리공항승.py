N, L = map(int, input().split())
D = list(map(int, input().split()))

D.sort()

def solution(N, L, D):
    d = 0
    answer = 0

    if N == 1:
        answer = 1
    elif N == 2:
        if (D[1] + 0.5) - (D[0] - 0.5) > L:
            answer = 2
        else:
            answer = 1
    else:
        for i in range(N-1):
            if d != 0:
                if d + D[i+1] - D[i] <= L:
                    d += D[i+1] - D[i]
                else:
                    answer += 1
                    d = 0
            else:
                if (D[i+1] + 0.5) - (D[i] - 0.5) <= L:
                    d += (D[i+1] + 0.5) - (D[i] - 0.5)
                else:
                    answer += 1
                    d = 0
        answer += 1
    return answer

print(solution(N, L, D))





