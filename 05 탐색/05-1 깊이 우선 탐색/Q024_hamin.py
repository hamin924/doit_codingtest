# 024 신기한 소수 찾기 (백준 2023번)
import sys
sys.setrecursionlimit(10**6)

n = int(input()) # 자릿 수 입력 받기

def isPrime(num): # 소수인지 판단하는 함수
    if n < 2:
        return False
    for i in range(2, int((num/2) + 1)):
        if num % i == 0:
            return False # 소수가 아님
    return True # 소수, 들여쓰기 잘해...

def DFS(num):
    if len(str(num)) == n: # 목표 길이 도달시 멈춤
        print(num)
    else:
        for i in range(10):
            if i % 2 == 0: # 짝수는 탐색 불필요
                continue
            if isPrime(num * 10 + i): # 소수이면 자릿수 늘림
                DFS(num * 10 + i) 

DFS(2)
DFS(3)
DFS(5)
DFS(7)

'''
에라토스테네스의 체를 이용하면 메모리 초과나므로 
그냥 소수 구하는 함수로 
'''