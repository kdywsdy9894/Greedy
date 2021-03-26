t = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    else:
        Fulldays = V//P*L
        if V%P <= L:
            answer = Fulldays + V%P
        else:
            answer = Fulldays + L
        print("Case {}: {}".format(t,answer))
        t += 1