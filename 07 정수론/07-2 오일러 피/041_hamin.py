# 041 오일러 피 함수 구현하기 (백준 11689번)
import math
n = int(input())
result = n

for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        result = result - result / i
        while n % i == 0: # n에서 소인수 제거
            n = n/i

if n > 1: # n이 마지막 소인수 일 때
    result = result - result / n

print(int(result))