# 006 연속된 자연수의 합 구하기 (백준 2018번)

n = int(input())

count = 1 # 자기 자신의 수 뽑는 경우 하나
sum = 1
start_index = 1
end_index = 1

while end_index != n : 
    if sum == n:
        count += 1
        end_index += 1
        sum = sum + end_index 
        
    elif sum > n:
        sum = sum - start_index # 순서 중요!
        start_index += 1
        

    else:
        end_index += 1
        sum = sum + end_index

print(count)