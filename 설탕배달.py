N = int(input())

def solution(N):
    a = N//5
    b = N - a*5
    while b%3 != 0:
        b += 5
        a -= 1
        if a < 0:
            return -1
    return a+b//3

print(solution(N))