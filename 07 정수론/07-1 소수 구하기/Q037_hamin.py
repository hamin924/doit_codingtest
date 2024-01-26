# 037 소수 구하기 (백준 1929번)
import math
m, n = map(int, input().split())
A = [0] * (n+1)


for i in range(2, n+1):
    A[i] = i

for i in range(2, int(math.sqrt(n)) + 1): # 제곱근 만큼 범위를 줄여 시간 줄임
    if A[i] == 0 : # 이미 지워졌으면 넘어감
        continue
    for j in range(i*2, n+1, i): # 배수 지우기
        A[j] = 0

for i in range(m, n+1):
    if A[i] != 0:
        print(A[i])