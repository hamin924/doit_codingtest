# 012 오큰수 구하기 (백준 17298번)

n = int(input())

A = list(map(int, input().split()))

stack = []
result = [0] * n # 정답 리스트

for i in range(n):
    while stack and A[stack[-1]] < A[i]: # 현재 수열(지금 들어오는 수열)이 스택 top 값보다 클 때
        result[stack.pop()] = A[i] # 정답 리스트에 오큰수 저장
    
    stack.append(i) # 스택에 오큰수의 인덱스 값 저장
    
while stack: # 스택이 아직 비어있지 않다면 -1 추가
    result[stack.pop()] = -1

answer = ' '.join(map(str, result)) # 리스트 문자열로 변환

print(answer)

'''
스택 사용
'''