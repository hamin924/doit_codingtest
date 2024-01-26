n = int(input())

A = list(map(int, input().split()))
A.sort()

left = 0
right = n-1

answer = abs(A[left] + A[right]) # 절댓값으로 바꿈
final = [A[left], A[right]] # 두 용액 값을 저장

while left < right:
    left_value = A[left]
    rigth_value = A[right]

    total = left_value + rigth_value

    if abs(total) < answer: # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담기
        answer = abs(total)
        final = [left_value, rigth_value]

    if total < 0: # 두 용액의 합이 0보다 작다면 왼쪽 값 늘려 더 0에 가깝게 만들기
        left += 1
    else: # 두 용액의 합이 0보다 크면 오른쪽 값을 줄여 조금 더 0에 가깝게 만들기
        right -= 1
    
print(final[0],final[1])