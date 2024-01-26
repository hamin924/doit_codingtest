# 085 퇴사 준비하기 (백준 14501번)
import sys
input = sys.stdin.readline

n = int(input())

D = [0] * (n+2)
T = [0] * (n+1) # 상담에 필요한 일 수
P = [0] * (n+1)  # 상담 완료 했을 때 받는 수입

for i in range(1, n+1):
    T[i], P[i] = map(int, input().split())


for i in range(n, 0, -1): # n+1부터 1까지
    if i + T[i] > n+1: # 오늘 시작된 상담이 퇴사일까지 끝나지 않는 경우
        D[i] = D[i+1]
    else:
        D[i] = max(D[i+1], P[i] + D[i+T[i]])

print(D[1])