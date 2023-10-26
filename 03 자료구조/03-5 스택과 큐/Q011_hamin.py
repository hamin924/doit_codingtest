# 011 스택으로 수열 만들기 (백준 1874번)

n = int(input())

A = [0] * n

for i in range(n):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = []

for i in range(n):
    while A[i] >= num: # 현재 수열의 값이 오름차순 num보다 작을 때 수열 값 만큼 push
        stack.append(num)
        answer.append("+")
        num += 1

    if stack[-1] == A[i]: # stack 마지막 값과 현재 수열의 값이 같으면 pop
        stack.pop()
        answer.append("-")

    else: # 현재 수열의 값보다 오름차순 num이 클 때 수열 출력 불가
        result = False
        break

if result == False:
    print("NO")

else:
    for i in answer:
        print(i)