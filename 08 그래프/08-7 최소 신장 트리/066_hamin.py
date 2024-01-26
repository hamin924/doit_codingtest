# 067 불우이웃 돕기 (백준 1414번)
import queue

n,m = map(int, input().split())
pq = queue.PriorityQueue()
parent = []

for i in range(m):
    pq[i] = list(map, int(input().split()))

def find(a):
    if a == parent[a] :
        return
    