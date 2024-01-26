# 044 칵테일 만들기 (백준 1033번)

n = int(input())
A = [[] for i in range(n)]

vistited = [False] * (n)
D = [0] * (n)
lcm = 1 # 최소 공배수

def gcd(a,b): # 최대 공약수 함수
    if b==0:
        return a
    else:
        return gcd(b, a % b) 

def DFS(node): # dfs 탐색 함수
    vistited[node] = True
    for i in A[node]:
        next = i[0]
        if not vistited[next]:
            D[next] = D[node] * i[2] // i[1] # 현재 노드의 값 * 비율
            DFS(next)
    
for i in range(n-1):
    a,b,p,q = map(int, input().split())
    A[a].append((b,p,q))
    A[b].append((a,q,p))
    lcm *= (p*q // gcd(p,q)) # 최소 공배수 = 두수의 곱/최대 공약수

D[0] = lcm # 최대 공약수
DFS(0)
mgcd = D[0] # 최대 공약수

for i in range(1,n):
    mgcd = gcd(mgcd, D[i])

for i in range(n):
    print(int(D[i] // mgcd), end=' ')

'''
트리 구조
'''