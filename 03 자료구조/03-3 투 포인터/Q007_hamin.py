# 007 주몽의 명령 (백준 1940번)
import sys 
input = sys.stdin.readline

n = int(input())
m = int(input())
A = list(map(int, input().split()))

A.sort()

count = 0
i = 0 # 시작은 0부터
j = n-1

while i < j:
    if A[i] + A[j] < m: # 작은 번호를 한칸 위로 이동
        i += 1 
    elif A[i] + A[j] > m: # 큰 번호를 한칸 아래로 이동
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1


print(count)