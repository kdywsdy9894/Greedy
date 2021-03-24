N = int(input())
P = list(map(int, input().split()))

def solution(N, P):
    answer = 0
    for i in range(len(P)):
        answer += sorted(P)[i]*(len(P)-i)
    return answer

print(solution(N, P))