n = int(input())

is_prime = [False, False] + [True] * (n-1) # 소수인지 판단 -> 에라토스테네스의 체!!
prime_num = []

for i in range(2, n+1):
    if is_prime[i]: # i가 소수일 때
        prime_num.append(i)
        for j in range(2*i, n+1, i): # i 배수들 false 판정
            is_prime[j] = False

count = 0 
start_index = 0
end_index = 0

while end_index <= len(prime_num) : 
    temp = sum(prime_num[start_index:end_index])
    if temp == n:
        count += 1
        end_index += 1
    
    elif temp < n:
        end_index += 1    

    else:
        start_index += 1

print(count)