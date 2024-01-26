# 082 사전 찾기 (백준 1256번)
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) # n: a 문자 수, m: z 문자 수, k: 순번
D=[[0 for j in range(202)] for i in range(202)]


for i in range(0, 201):
    for j in range(0, i+1): # 고르는 수의 개수가 전체 개수를 넘을 수 없으므로 i번째까지
        if j == 0 and j == i:
            D[i][j] = 1
        else:
            D[i][j] = D[i-1][j] + D[i-1][j-1]
            if D[i][j] > 1000000000: # k 범위가 넘어가면 범위의 최댓값 저장
                D[i][j] = 1000000001

if D[n+m][m] < k:
    print(-1)
else:
    while n != 0 or m != 0: # or로 연결해야함
        if D[n-1+m][m] >= k: # a를 선택해도 남은 경우의 수가 k 보다 큰 경우
            print('a', end='')
            n -= 1
        else:
            print('z', end='')
            k -= D[n-1+m][m]
            m -= 1
