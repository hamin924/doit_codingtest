# 034 수를 묶어서 최댓값 만들기 (백준 1744번)

n = int(input())
plus = []
minus = []
sum = 0

for i in range(n):
    data = int(input())
    if data <= 0:
        minus.append(data)
    elif data > 1:
        plus.append(data)
    else:
        sum += data

plus.sort(reverse=True) # 3 2 1
minus.sort() # -3 -2 -1

for i in range(0, len(plus), 2): # 양수 묶기
    if i+1 >= len(plus):
        sum += plus[i]
    else:
        sum += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2): # 음수 묶기
    if i+1 >= len(minus):
        sum += minus[i]
    else:
        sum += (minus[i] * minus[i+1])

print(sum)