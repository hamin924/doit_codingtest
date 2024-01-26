# 투 포인터
import sys

n, m = map(int,input().split())

A = []

for i in range(n):
    A.append(int(input().rstrip()))

A.sort()

start = 0
end = 0
min_value = sys.maxsize

while start < n and end < n : 
    result = A[end] - A[start]
    if result >= m:
        min_value = min(A[end] - A[start], min_value)
        start += 1
    else:
        end += 1

print(min_value)