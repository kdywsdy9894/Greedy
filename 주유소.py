N = int(input())
distance = list(map(int, input().split()))
price_per_liter = list(map(int, input().split()))

min_price = 0
price = price_per_liter[0]
d = 0

for i in range(len(distance)):
    if price >= price_per_liter[i+1]:
        if d == 0:
            min_price += price*distance[i]
            price = price_per_liter[i+1]
        else:
            min_price += price*(d+distance[i])
            price = price_per_liter[i+1]
            d = 0
    else:
        d += distance[i]
if d != 0:
    min_price += price*d
    
print(min_price)



