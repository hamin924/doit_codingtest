# 090 최장 공통 부분 수열 찾기(LCS) (백준 9252번)
import sys
sys.setrecursionlimit(10**6) # 재귀 최대 깊이 설정
input = sys.stdin.readline

a = list(input())
a.pop() # \n문자열 제거
b = list(input())
b.pop() # \n문자열 제거

D=[[0 for j in range(len(b)+1)] for i in range(len(a)+1)] # 행 먼저, 열 나중에

path = []

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]: # 같은 문자열이면 왼쪽 대각선 값 + 1
            D[i][j] = D[i-1][j-1] + 1 
        else: # 다르면 왼쪽과 위의 값 중 큰수
            D[i][j] = max(D[i-1][j], D[i][j-1])

print(D[len(a)][len(b)])

def getText(row, col): # 재귀 형태
        if row == 0 or col == 0:
             return
        if a[row-1] == b[col-1]: # 같으면 왼쪽 위로 이동
             path.append(a[row-1])
             getText(row-1, col-1)
        else:
             if D[row -1][col] > D[row][col-1]: # 왼쪽 값이 더크면 왼쪽으로 이동
                  getText(row-1,col)
             else: # 위쪽 값이 더 크면 위쪽으로 이동
                  getText(row,col-1)

getText(len(a), len(b))

for i in range(len(path)-1,-1,-1):
    print(path.pop(i), end="")