# 문자열 생성, 그리디(투포인터)

n = int(input())
arr = []

for i in range(n):
    arr.append(input())

answer = ""

left = 0 # 시작은 0부터
right = len(arr)-1

while left <= right:
    if arr[left] > arr[right]:
        answer += arr[right]
        right -= 1
    elif arr[left] < arr[right]: # 큰 번호를 한칸 아래로 이동
        answer += arr[left]
        left += 1
    else: # 같은 문자인 경우
        temp_left = left + 1
        temp_right = right - 1
        flag = 0
        while temp_left <= temp_right:
            if arr[temp_left] < arr[temp_right]:
                flag = 1
                break

            elif  arr[temp_left] > arr[temp_right]:
                flag = 2
                break
            temp_left += 1
            temp_right -= 1
        if flag == 1:
            answer +=arr[left]
            left += 1
    
        elif flag == 2:
            answer += arr[right]
            right -= 1
        else: # 문자열 전부 같을때
            answer += arr[left]
            left += 1
         
answer = list(answer)
count = 0

for i in answer:
    print(i, end='')
    count += 1
    if count % 80 == 0: # 80글자마다 새 줄 출력
        print()