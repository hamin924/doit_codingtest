# 084 정수를 1로 만들기 (백준 1463번)

n = int(input())
D = [0] * (n+1)

for i in range(2, n+1):
    D[i] = D[i-1] + 1 # -1 연산

    if i % 3 == 0: # if elif 사용하면 안됨, if문으로 세연산 다 거칠수 있게 해야함
        D[i] = min(D[i], D[i // 3] + 1)

    if i % 2 == 0:
        D[i] = min(D[i], D[i // 2] + 1)
        

print(D[n])
