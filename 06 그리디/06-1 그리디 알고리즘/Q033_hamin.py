# 033 카드 정렬하기 (백준 1715번)
# 우선순위 큐
from queue import PriorityQueue

n = int(input())
pq = PriorityQueue() # 우선 순위 큐는 오름차순으로 자동 정렬


for i in range(n):
    data = int(input())
    pq.put(data)

data1, data2, sum = 0, 0, 0

while pq.qsize() > 1:
    data1 = pq.get() 
    data2 = pq.get()
    temp = data1 + data2
    sum += temp
    pq.put(temp)

print(sum)