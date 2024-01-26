# 092 빌딩 순서 구하기 (백준 1328번) - 플래티넘

n, l, r = map(int,input().split())
mod = 1000000007

D = [[[0 for k in range(101)] for j in range(101)] for i in range(101)]
D[1][1][1] = 1 # 건물이 1개일때 경우의 수는 1개

for i in range(2, n+1):
    for j in range(1, l+1):
        for k in range(1, r+1):
            D[i][j][k] = D[i-1][j][k] * (i-2) + D[i-1][j][k-1] + D[i-1][j-1][k]
            D[i][j][k] = (D[i][j][k]) % mod

print(D[n][l][r])
