# 010 최솟값 찾기 1 (백준 11003번)
from collections import deque

n, l = map(int,input().split())

mydeque = deque()
now = list(map(int, input().split()))

for i in range(n):
    while mydeque and mydeque[-1][0] > now[i]: # 덱의 마지막 값이 입력받은 값 보다 클때
        mydeque.pop()

    mydeque.append((now[i],i)) # 덱의 마지막 위치에 값 저장
    
    if mydeque[0][1] <= i - l: # 범위를 벗어난 값은 덱에서 제거
        mydeque.popleft()

    print(mydeque[0][0], end=' ') # 제일 첫번째 값 출력