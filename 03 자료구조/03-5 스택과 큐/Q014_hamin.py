# 014 절댓값 힙 구현하기 (백준 11286번)
from queue import PriorityQueue
import sys
print = sys.stdout.write # 속도 개선
input = sys.stdin.readline

n = int(input())

queue = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        if queue.empty(): # 큐가 비어있으면 0 출력
            print('0\n')
        else: # 비어있지 않으면 절댓값이 작은 값 출력
            temp = queue.get()
            print(str((temp[1]))+'\n')
    else:
        queue.put((abs(request), request)) # 절댓값 기준으로 정렬하고 절댓값 같으면 작은 수(음수) 우선으로 정렬


'''
우선순위 큐에 정렬 기준을 새로 적용하는 방법
스레드의 안전을 요구하는 상황에서는 PriorityQueue, 아니라면 heapq를 사용하는 것이 좋다.
heapq 속도가 더 빠르다.
'''