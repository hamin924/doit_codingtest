# 091 가장 큰 정사각형 찾기 (백준 1915번)
import sys
input = sys.stdin.readline

D = [[0 for j in range(1001)] for i in range(1001)]
row, col = map(int, input().split())
result = 0 # 변수명 주의 max라고 쓰면 안돼

for i in range(0, row):
    numbers = list(input()) # 데이터를 한줄씩 저장하는 리스트
    for j in range(0, col):
        D[i][j] = int(numbers[j])
        if D[i][j] ==  1 and j > 0 and i > 0:
            D[i][j] = min(D[i-1][j-1], D[i][j-1], D[i-1][j]) + 1 # 점화식
        result = max(result, D[i][j])

print(result * result)
