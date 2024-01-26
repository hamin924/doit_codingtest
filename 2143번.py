# 투 포인터 활용

from collections import defaultdict

t = int(input())

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

answer = 0
A_dict = defaultdict(int) # 디폴트가 int인 딕셔너리

for i in range(n):
    for j in range(i, n):
        A_dict[sum(n_list[i:j+1])] += 1 

for i in range(m):
    for j in range(i, m):
        answer += A_dict[t - sum(m_list[i:j+1])]

print(answer)