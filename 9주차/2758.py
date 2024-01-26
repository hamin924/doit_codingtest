# DP 문제 - 로또
T = int(input())
DP = [[0]* 2001 for i in range(11)]
DP[0] = [1]*2001

for i in range(T):
    n,m = map(int, input().split())
    for i in range(1,11):
        for j in range(1,2001):
            DP[i][j] = DP[i][j-1] + DP[i-1][j//2] 
    
    print(DP[n][m])
