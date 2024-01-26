# 038 거의 소수 구하기 (백준 1456번)
import math
min, max = map(int, input().split())
A = [0] * (10000001)

for i in range(2,len(A)):
    A[i]=i

for i in range(2, int(math.sqrt(len(A)) + 1)): # 먼저 소수를 찾고,
    if A[i] == 0: # 소수 아니면 넘어감
        continue
    for j in range(i+i, len(A), i): # 배수 지우기
        A[j] = 0
    
count = 0

# 변수 표현 범위 넘어가지 않도록
for i in range(2, len(A)):
    if A[i] != 0: # 소수 중에서 범위 넘어가지 않는 값 찾음
        temp = A[i]
        while A[i] <= max / temp:
            if A[i] >= min /temp:
                count += 1
            temp = temp * A[i] # n제곱 표현


print(count)