import sys
input = sys.stdin.readline

n = int(input())
hw = [list(map(int, input().split())) for _ in range(n)]

hw.sort()
can_hw = [] # 해당 일수에 가능한 과제 저장 리스트
result = 0

for date in range(n, 0, -1): # 마지막 일수부터 가장 처음 일수까지 반복
    while hw and hw[-1][0] >= date : # 해당 날짜에 수행할 수 있는 과제점수 리스트
        can_hw.append(hw.pop()[1]) # 그 과제의 점수 pop

    if can_hw: # 해당 날짜에 수행할 수 있는 과제 있으면
        can_hw.sort() # 점수 큰 순서대로 정렬
        result += can_hw.pop()

print(result)


'''
자료구조 - 우선순위 큐를 이용해서도 풀 수 있음
'''