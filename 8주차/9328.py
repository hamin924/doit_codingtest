# 열쇠 (BFS 문제)
import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(visited):
    global result
    queue = deque([[0,0]])
    visited[0][0] = True
    while queue:
        r, c = queue.popleft() # row, col

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위를 벗어나거나 벽이거나 이미 방문한경우 예외처리
            if nc < 0 or nc >= w+2 or nr < 0 or nr >= h+2 or miro[nr][nc] == '*' or visited[nr][nc]:
                continue
            if 'A' <= miro[nr][nc] <= 'Z': # 대문자(문)이라면
                # 해당 문을 열 수 있는 키가 없다면
                if chr(ord(miro[nr][nc]) + 32) not in key : # ord : 해당 문자열의 유니코드 정수 반환
                    continue
            elif 'a' <= miro[nr][nc] <= 'z': # 소문자(열쇠)라면
                if miro[nr][nc] not in key: # 아직 키가 없다면
                    key[miro[nr][nc]] = True # 해당 키 저장 후
                    visited = [[False] * (w+2) for _ in range(h+2)] # 방문 체크 초기화
            elif miro[nr][nc] == '$' and (nr, nc) not in visited_doc: # 찾는 문서이고 아직 방문하지 않았다면
                result += 1
                visited_doc.append((nr, nc)) # 해당 위치는 다시 방문하지 않기 위해 저장
            visited[nr][nc] = True
            queue.append([nr, nc]) # 다음 위치를 큐에 삽입



T = int(input())

for i in range(1, T+1):
    h, w = map(int, input().split())

    miro = ['.' + input() + '.' for i in range(h)]
    miro = ['.' * (w+2)] + miro + ['.' * (w+2)]
    visited = [[False] * (w+2) for i in range(h+2)]
    key = {} # 가지고 있는 키 저장
    visited_doc = [] # 방문한 키 위치 저장

    for i in input():
        if i.isalpha(): # 만약 알파벳이면
            key[i] = True
    
    result = 0
    BFS(visited)
    print(result)
        

'''
set, map을 이용한 방법도 있음
'''