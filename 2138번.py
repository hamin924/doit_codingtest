# 그리디
n = int(input())

before = list(map(int,input()))
target = list(map(int, input()))

def change(A,B):
    A_copy = A[:]
    press = 0
    for i in range(1, n): # 이전 전구가 같은 상태면 pass
        if A_copy[i-1] == B[i-1]:
            continue
        press += 1 # 상태가 다른 경우
        for j in range(i-1, i+2):
            if j < n:
                A_copy[j] = 1 - A_copy[j]
    
    return press if A_copy == B else 1e9

res = change(before, target) # 첫번째 전구의 스위치를 누르지 않은 경우
before[0] = 1 - before[0]
before[1] = 1 - before[1]

res = min(res, change(before,target) + 1) # 첫번째 전구를 눌렀을 때와 안눌렀을 때 최솟값
print(res if res!= 1e9 else -1)

'''
가운데를 누르면 양옆이 누르는 것을
첫번째를 눌렀을 때 뒤에 2값이 면하는 것
=> pivot의 위치를 바꾸는 것
'''