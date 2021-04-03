S = input()

def solution(S):
    _S = list()
    _S.append(S[0])
    for i in range(1,len(S)):
        if S[i-1] != S[i]:
            _S.append(S[i])
    if _S.count('0') >= _S.count('1'):
        return _S.count('1')
    else:
        return _S.count('0')
        
print(solution(S))


        


            