# 049 물의 양 구하기 (백준 2251번)
from collections import deque

a, b, c = map(int, input().split())

# 경우의 수를 담을 큐
q = deque()
q.append((0, 0)) # a,b 값 초기화

# 방문 여부 저장
visited = [[False] * (b + 1) for _ in range(a + 1)]
visited[0][0] = True

answer = []

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))
        
def bfs():
    while q:
        # A물통에 있는 물: x, B물통에 있는 물: y, C물통에 있는 물: z
        x, y = q.popleft()
        z = c - x - y # c는 자기 전체 물 양에서 a와 b 뺀 값
        
        # A 물통이 비어있는 경우에 C 물통에 남아있는 양 저장
        if x == 0:
            answer.append(z)
            
        # A에서 B로 물 이동
        water = min(x, b - y) # x전체를 옮기거나 b물통을 꽉 채우는 방법
        pour(x - water, y + water) # 옮긴 후 x,y 상태 큐를 저장
        # A에서 C로 물 이동
        water = min(x, c - z)
        pour(x - water, y)
        
        # B에서 C로 물 이동
        water = min(y, c - z)
        pour(x, y - water)
        # B에서 A로 물 이동
        water = min(y, a - x)
        pour(x + water, y - water)
        
        # C에서 A로 물 이동
        water = min(z, a - x)
        pour(x + water, y)
        # C에서 B로 물 이동
        water = min(z, b - y)
        pour(x, y + water)
        
bfs()

answer.sort()
for i in answer:
    print(i, end=" ")
