# 035 회의실 배정하기 (백준 1931번)

n = int(input())

A = [[0] * 2 for _ in range(n)]

for i in range(n):
    start, end = map(int,input().split())
    A[i][0] = end # 종료 시각으로 우선 정렬하기위해
    A[i][1] = start

A.sort()
count = 0
end = 0

for i in range(n):
    if A[i][1] >= end:
        end = A[i][0] # 현재 회의 종료시각으로 업데이트
        count += 1
    

print(count)