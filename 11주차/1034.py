# 램프, 브루트포스 알고리즘

n, m = map(int, input().split())
lamp = []
for i in range(n):
    line = list(map(int,list(input())))
    lamp.append(line)
k = int(input())

cnt = [0] * n

if k % 2: # k가 짝수 일 때
    for i in range(n):
        zero_cnt = lamp[i].count(0)
        if zero_cnt % 2 and zero_cnt <= k: # 0의 갯수가 짝수일때
            for j in range(n):
                if lamp[i] == lamp[j]:
                    cnt[i] += 1
else:
    for i in range(n):
        zero_cnt = lamp[i].count(0) # 0 갯수 카운트
        if not zero_cnt % 2 and zero_cnt <= k: # 0의 갯수가 홀수 일 때
            for j in range(n):
                if lamp[i] == lamp[j]:
                    cnt[i] += 1

print(max(cnt))