import sys

T = int(sys.stdin.readline())

for i in range(T):
    case = list()
    N = int(sys.stdin.readline())
    for j in range(N):
        case.append(list(map(int, sys.stdin.readline().split())))
    
    rank = list(sorted(case, key = lambda x: x[0]))
    
    min_rank = rank[0][1]
    
    answer = 0
    for k in range(1,len(rank)):
        if rank[k][1] < min_rank:
            min_rank = rank[k][1]
            answer += 1

    print(answer)

    