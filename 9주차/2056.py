# 위상 정렬, DP문제 - 작업

n = int(input())
DP = [0] * (n+1)

for i in range(1, n+1):
    cost, count, *pre = map(int, input().split())
    DP[i] = cost
    for j in pre:
        DP[i] = max(DP[i], DP[j] + cost)
        
print(max(DP))
