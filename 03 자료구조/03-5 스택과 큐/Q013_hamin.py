# 013 카드 게임 (백준 2164번)
from collections import deque

n = int(input())

queue = deque()

for i in range(1, n+1): # 숫자 1부터
    queue.append(i)

while len(queue) > 1: # 카드가 한 장 남을때 까지
    queue.popleft() # 맨 위 카드 버림
    temp = queue.popleft() 
    queue.append(temp) # 맨 위 카드를 가장 아래 밑으로 이동

print(queue[0])