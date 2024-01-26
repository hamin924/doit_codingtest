# 017 내림차순으로 자릿수 정렬하기 (백준 1427번)

A = list(input())

for i in range(len(A)):
    max = i
    for j in range(i+1, len(A)):
        if A[max] < A[j]: # 최댓값 찾기
            max = j

    if A[i] < A[max]:
        temp = A[max]
        A[max] = A[i]
        A[i] = temp
    
print(''.join(map(str, A))) # 리스트 문자열로 표현