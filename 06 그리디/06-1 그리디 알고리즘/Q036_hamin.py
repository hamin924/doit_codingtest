# 036 최솟값을 만드는 괄호 배치 찾기 (백준 1541번)

answer = 0
A=list(map(str, input().split('-')))

def Sum(string): # -로 나눈 그룹들의 합
    sum = 0
    temp = str(string).split('+')
    for i in temp:
        sum += int(i)
    
    return sum

for i in range(len(A)):
    temp = Sum(A[i])
    if i == 0: 
        answer += temp # 0 + temp
    else:
        answer -= temp

print(answer)