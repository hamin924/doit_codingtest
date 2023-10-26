# 009 DNA 비밀 번호 (백준 12891번)

checkList = [0] * 4 # 비밀번호 체크 리스트
myList = [0] * 4 # 현재 상태 리스트
checkSecret = 0

def myadd(k): # 새로 들어오는 문자를 처리하는 함수
    global checkList, myList, checkSecret
    if k == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif k == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif k == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif k == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(k): #제거되는 문자를 처리하는 함수
    global checkList, myList, checkSecret
    if k == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif k == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif k == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif k == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1


S, P = map(int, input().split())
count = 0

data = list(input()) # 함수명 자주쓰이는 예약어로 하면 안됨

checkList = list(map(int, input().split()))


for i in range(4): 
    if checkList[i] == 0: # 값이 0이면 비밀번호 개수가 이미 만족되었다는 뜻
        checkSecret += 1

for i in range(P): # 초기 리스트의 문자열 처리
    myadd(data[i])

if checkSecret == 4:
    count += 1

for i in range(P,S):
    j = i - P
    myadd(data[i])
    myremove(data[j])
    if checkSecret == 4:
        count += 1

print(count)