# 081 순열의 순서 구하기 (백준 1722번)
import sys
input = sys.stdin.readline

F = [0] * 21
S = [0] * 21
visited = [False] * 21
n = int(input())
F[0] = 1

for i in range(1, n+1):
    F[i] = F[i-1] * i # 팩토리얼 공식

inputList = list(map(int, input().split())) # 순열 위치, 문자열 입력

if inputList[0] == 1: # 순열을 출력하는 문제
    k = inputList[1]
    for i in range(1, n+1):
        count = 1
        for j in range(1, n+1):
            if visited[j] == True:
                continue
            if k <= F[n-i] * count:
                k = k - F[n-i] * (count-1) # 현재 자리 순열 수 : n-i
                S[i] = j
                visited[j] = True
                break
            count += 1
    for i in range(1, n+1):
        print(S[i], end=' ')
else: # 순열의 순서를 출력하는 문제
    k = 1
    for i in range(1, n+1):
        count = 0
        for j in range(1, inputList[i]):
            if visited[j] != True:
                count += 1
        
        k = k + count * F[n-i] # 자릿수에 따라 순서 더하기
        visited[inputList[i]] = True
    print(k)


