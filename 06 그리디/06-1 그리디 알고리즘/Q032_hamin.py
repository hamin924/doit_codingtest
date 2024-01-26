# 032 동전 개수의 최솟값 구하기 (백준 11047번)

n, k = map(int, input().split())

A = [0] * n

for i in range(n):
    A[i] = int(input())

count = 0

for i in range(n-1, -1, -1): # 역순으로 진행
    if k >= A[i]: # 구할 금액보다 동전 리스트가 작을 때
        count += int(k / A[i])
        k = k % A[i]

print(count)