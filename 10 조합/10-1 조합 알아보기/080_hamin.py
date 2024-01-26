# 080 조약돌 꺼내기 (백준 13251번)

M = int(input()) # 색 종류
D = list(map(int,input().split()))
T = 0
K = int(input()) # 선택 조약돌 개수
probability = [0] * 51
answer = 0

for i in range (0, M):
    T += D[i]

for i in range(0, M):
    if D[i] >= K:
        probability[i] = 1

        for k in range(0,K): # 자릿수 만큼 반복
            probability[i] = probability[i] * (D[i]-k)/(T-k)

        answer += probability[i]

print(answer)


'''
처음엔 각각의 경우의 수 구해서 마지막에 전체 경우의 수에서 나눌려고 했지만
실패..
'''