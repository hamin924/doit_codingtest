# 호텔, DP 배낭문제

c, n = map(int, input().split())

cost_list = [list(map(int,input().split())) for _ in range(n)] # 비용과 비용으로 얻을 수 있는 고객수
dp = [1e7 for _ in range(c+100)]
dp[0]=0 # 0명 모을 땐, 0원
 
for cost, num_people in cost_list: # 각 비용, 비용으로 얻을 수 있는 고객수에 대해
    for i in range(num_people, c+100): # num_people 부터 C+100 까지 반복
        dp[i] = min(dp[i-num_people]+cost, dp[i]) # i명일 때, 최소비용 갱신
 
print(min(dp[c:]))