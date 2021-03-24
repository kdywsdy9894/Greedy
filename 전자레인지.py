T = int(input())

count_300 = T//300
count_60 = T%300//60
count_10 = T%300%60//10

if T%300%60%10 != 0:
    print (-1)
else:
    print(count_300, count_60, count_10)