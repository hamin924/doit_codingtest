# 087 2 x n 타일 채우기 (백준 11726번)

n = int(input())

D = [0] * (1001)
D[1] = 1 # 2x1 일때 타일의 경우의 수 
D[2] = 2 # 2x2 일때 타일의 경우의 수 

for i in range(3, n+1): # 3 ~ n 범위
    D[i] = (D[i-1] + D[i-2]) % 10007

print(D[n])