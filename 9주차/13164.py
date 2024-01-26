# 그리디, 정렬 - 행복 유치원
n, k = map(int,input().split())
kids = list(map(int,input().split()))

array = [] # 키 차이 저장 배열

for i in range(1,n):
    array.append(kids[i] - kids[i-1])

array.sort(reverse=True)

print(sum(array[k-1:]))
