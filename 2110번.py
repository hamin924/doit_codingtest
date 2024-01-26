# 이진 탐색
n, c = map(int,input().split())

A = []

for i in range(n):
    A.append(int(input()))

A.sort()

start = 1
end = A[-1] - A[0] # 공유기사이 거리 최대
result = 0

while start <= end:
    mid = int((start+end)/2)
    current = A[0]
    count = 1 # 첫번째 공유기는 무조건 설치

    for i in range(1, len(A)): # 공유기 설치 몇 대 가능한지 체크
        if A[i] >= current + mid:
            count += 1
            current = A[i]

    if count >= c: # 공유기 설치 수가 받은 값보다 크면 공유기 사이 거리 늘림
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)