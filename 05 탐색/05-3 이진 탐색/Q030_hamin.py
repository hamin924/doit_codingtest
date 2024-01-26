# 030 블루레이 만들기 (백준 2343번)

n, m = map(int, input().split())

A = list(map(int, input().split()))


start = max(A) # 최댓값을 시작 인덱스로 저장
end = sum(A) # 레슨의 총합을 종료 인덱스로 저장

while start <= end:
    mid_index = int((start+end)/2)
    sum = 0
    count = 0
    for i in range(n): # 중간 값으로 모든 레슨을 저장할 수 있는지 확인
        if sum + A[i] > mid_index:
            count += 1
            sum = 0 # 현재 블루레이에 저장할 수 없어 새로운 블루레이로 교체
        sum += A[i]

    if sum != 0:
        count += 1
    if count > m: # 정해진 블루레이 갯수보다 크면 start값 증가
        start = mid_index + 1
    else:
        end = mid_index - 1

print(start)