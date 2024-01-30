# 용액 합성하기, 투 포인터
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))


start_index = 0
end_index = n-1
result = A[start_index] + A[end_index]

while start_index < end_index:
    temp = A[start_index] + A[end_index]
    if abs(result) > abs(temp):
        result = temp
    if temp < 0:
        start_index += 1
    else:
        end_index -= 1

print(result)