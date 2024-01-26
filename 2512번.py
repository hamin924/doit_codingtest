# 이분 탐색

n = int(input())

A = list(map(int, input().split()))

budgets = int(input())  # 총 예산

start = 0
end = max(A)

while start <= end:
    mid = int((start+end)/2) # 상한액 설정
    total = 0
    for i in A:
        if i > mid: # 요청한 금액이 상한액 이상이면
            total += mid
        else: # 요청한 금액이 상한액 미만이면
            total += i

    if total <= budgets: # 예산보다 작으면 start 값을 올려 total 값 올려줌
        start = mid + 1 
    else: 
        end = mid -1

print(end)