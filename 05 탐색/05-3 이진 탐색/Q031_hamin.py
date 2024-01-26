# 031 배열에서 K번째 수 찾기 (백준 1300번)

n = int(input())
k = int(input())

start = 1
end = k
result = 0

while start <= end:
    middle_index = int((start+end) / 2)
    count = 0
    for i in range(1,n+1):
        count += min(int(middle_index / i), n) # 행의 크기(n)는 넘어가지 못함
    if count < k:
        start = middle_index + 1
    else:
        result = middle_index
        end = middle_index - 1

print(result)


'''
나만의 전략을 세울줄 알아야함
10을 구할때는 9를 구해서 다음 순서를 생각해라
'''