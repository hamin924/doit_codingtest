# 배낭 문제(knapsack 알고리즘)

n, k = map(int, input().split())
ob = [[0,0]]
D = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    ob.append(list(map(int, input().split())))
   

for i in range(1, n+1): # n개 만큼
    for j in range(1, k+1): # 총 무게 만큼
        w = ob[i][0]
        v = ob[i][1]
        if j < w: # 넣을 물건 무게가 현재 무게보다 크면 넣지 않음
            D[i][j] = D[i-1][j]
        else:
            D[i][j] = max(D[i-1][j-w] + v, D[i-1][j]) 
            # 현재 넣을 물건 무게만큼 배낭에서 빼고 현재 물건 넣거나 현재 물건 넣지 않고 이전 배낭 무게


print(D[n][k])
        

'''
냅색 알고리즘
0-1 배낭 문제 : 담을지 안담을지 정하는 문제
'''