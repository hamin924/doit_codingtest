# union-find 알고리즘
import sys
input = sys.stdin.readline


def find(x): # 부모 노드 찾기
    if x == parents[x]: # 자신이 부모 노드이면 자신 return
        return x
    else:
        parents[x] = find(parents[x]) # 재귀함수형태
        return parents[x]
    

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b: # 부모 노드가 같으면 return
        return network[a]
    else:
        parents[b] = a # 부모 노드가 다르면 b의 부모노드를 a로 바꿔줌
        network[a] += network[b]

T = int(input())

for i in range(T):
    n = int(input())
    parents = dict()
    network = dict()
    for i in range(n):
        a, b = map(str, input().split())
        
        # 친구 관계의 없는 친구이면 추가해줌
        # 연결 수도 추가해줌
        if a not in parents:
            parents[a] = a
            network[a] = 1

        if b not in parents:
            parents[b] = b
            network[b] = 1

        union(a,b)

        print(network[find(a)])
        
'''
network도 똑같이 병합을 했다
'''