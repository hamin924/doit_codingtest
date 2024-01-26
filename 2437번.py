n = int(input())
A = list(map(int,input().split()))

A.sort()

target = 0

for i in A:
    if target < i: # 리스트 값이 target보다 크면 만들수 없는 금액의 최솟값
        break
    else:
        target += i

target = target + 1

print(target)

'''
1 1 2 3 6 7 30
'''