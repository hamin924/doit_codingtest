# 004 구간 합 구하기 2 (백준 11660번)
import sys 
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 숫자 개수, 질의 개수

A=[] #원본 리스트
D=[[0]*(n+1) for k in range(n+1)] #합의 배열

for i in range(n):
    A_row = list(map(int, input().split())) # 한 행씩 입력받기
    A.append(A_row)


for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i-1][j-1] # 합 배열 저장

for k in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1] # 질의에 대한 결과 계산 및 출력
    print(result)