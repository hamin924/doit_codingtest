# 003 구간 합 구하기 1 (백준 11659번)
import sys # 반복문 안에서 input()을 사용하므로 선언
input = sys.stdin.readline 

n, m = map(int, input().split()) # n: 숫자 개수, 질의 개수

numbers=list(map(int, input().split())) # 숫자 데이터 저장

prefix_sum=[0] #초깃 값 0 저장!!, 합 배열

temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)

for k in range(m):
    s, e= map(int, input().split())

    print(prefix_sum[e] - prefix_sum[s-1])