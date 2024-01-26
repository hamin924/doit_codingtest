# 백트래킹 문제 , DFS
import sys
input = sys.stdin.readline

n = int(input())
result = 0
row = [0] * n

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i): # 같은 열이나 대각선 방향 확인
            return False
    return True

def n_queens(x):
    global result
    if x == n: # n행으로 가면 성공
        result += 1
        return
    else:
        for i in range(n):
            row[x] = i # [i,x]에 퀸을 둔다
            if check(x): 
                n_queens(x+1)

n_queens(0)
print(result)



'''
퀸이 서로 공격할 수 없는 방법
1. 같은 행에 위치하면 안됨
2. 같은 열에 위치하면 안됨
3. 대각선상에 위치하면 안됨
'''