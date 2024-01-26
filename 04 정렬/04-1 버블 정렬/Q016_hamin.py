# 016 버블 정렬 프로그램 1 (백준 1377번)
import sys
input = sys.stdin.readline

n = int(input())

A = [] # 리스트는 하나의 변수만 저장 가능

for i in range(n):
    A.append((int(input()),i)) # 인덱스 저장
    
max = 0
A_sort = sorted(A)


for i in range(n):
    if max < A_sort[i][1] - i: # 정렬 전 index - 정렬 후 index 계산해 최댓값 저장
        max = A_sort[i][1] - i

print(max+1)
    

'''
정렬을 맞친 시점이 몇회 차인지 구하는 문제
'''