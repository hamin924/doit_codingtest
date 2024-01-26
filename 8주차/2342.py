# DP 문제
import sys
sys.setrecursionlimit(10**6)
 
def move(a, b): # a -> b로 이동
    if a == b: # 같은 위치
        return 1
    elif a == 0: # 중앙위치에서 다른 곳
        return 2
    elif abs(b-a)%2 == 0: # 반대편
        return 4
    else:
        return 3
 
def solve(n, l, r):
    global dp
    if n >= len(arr)-1:
        return 0
 
    if dp[n][l][r] != -1:
        return dp[n][l][r]
 
    dp[n][l][r] = min(solve(n+1, arr[n],r) + move(l, arr[n]), solve(n+1, l, arr[n]) + move(r, arr[n]))
    return dp[n][l][r]
 
arr = list(map(int, sys.stdin.readline().split()))
dp = [[[-1]*5 for _ in range(5)] for _ in range(100000)]
 
print(solve(0, 0, 0))