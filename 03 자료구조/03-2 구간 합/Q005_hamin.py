# 005 나머지 합 구하기 (백준 10986번)
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))

S = [0] * n # 합 배열
C = [0] * m
S[0] = A[0]

answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i] # 합 배열 저장

for i in range(n):
    remainder = S[i] % m # 합 배열에서 나머지 구하기
    if remainder == 0: # m의 배수일 때 정답에 1 더하기
        answer += 1
    C[remainder] += 1 # 나머지가 같은 인덱스 개수 값 증가시키기

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2) # /는 float형, //는 int형

print(answer)